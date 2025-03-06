import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as tb
from google.cloud import texttospeech
import os
from playsound import playsound  # Substitui pygame para reprodução de áudio


class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Converter")
        self.root.geometry("500x400")
        self.root.resizable(True, True)  # Permitir redimensionamento
        self.style = tb.Style(theme="darkly")  # Aplicando o tema escuro

        # Variável para armazenar a lista de vozes
        self.voices = []

        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Entrada para a API Key
        ttk.Label(main_frame, text="API Key:").pack(anchor="w")
        self.api_key_entry = ttk.Entry(main_frame, width=50, show="*")
        self.api_key_entry.pack(pady=5, fill="x")

        # Botão para carregar vozes
        self.load_voices_button = ttk.Button(main_frame, text="Carregar Vozes", command=self.load_voices)
        self.load_voices_button.pack(pady=5, fill="x")

        # Caixa de texto
        ttk.Label(main_frame, text="Texto para conversão:").pack(anchor="w")
        self.text_entry = tk.Text(main_frame, height=5, wrap="word")
        self.text_entry.pack(pady=5, fill="x")

        # Escolher voz
        ttk.Label(main_frame, text="Escolher voz:").pack(anchor="w")
        self.voice_selection = ttk.Combobox(main_frame, state="readonly")
        self.voice_selection.pack(pady=5, fill="x")

        # Ajustar velocidade
        ttk.Label(main_frame, text="Velocidade da voz:").pack(anchor="w")
        self.speed_scale = ttk.Scale(main_frame, from_=0.5, to=2.0, orient="horizontal")
        self.speed_scale.set(1.0)
        self.speed_scale.pack(pady=5, fill="x")

        # Rótulo para exibir a velocidade atual
        self.speed_label = ttk.Label(main_frame, text="Velocidade: 1.0")
        self.speed_label.pack(anchor="w")

        # Configurar o comando do slider APÓS criar o speed_label
        self.speed_scale.config(command=self.update_speed_label)

        # Botão de teste
        self.test_button = ttk.Button(main_frame, text="Testar", command=self.test_audio)
        self.test_button.pack(pady=5, fill="x")

        # Botão de conversão
        self.convert_button = ttk.Button(main_frame, text="Converter", command=self.convert_text)
        self.convert_button.pack(pady=5, fill="x")

        # Botão de download
        self.download_button = ttk.Button(main_frame, text="Download Áudio", command=self.download_audio)
        self.download_button.pack(pady=5, fill="x")

        self.audio_file = None

    def update_speed_label(self, value):
        """Atualiza o rótulo da velocidade com o valor atual."""
        self.speed_label.config(text=f"Velocidade: {float(value):.1f}")

    def load_voices(self):
        """Carrega a lista de vozes disponíveis da API do Google Cloud Text-to-Speech."""
        api_key = self.api_key_entry.get().strip()
        if not api_key:
            messagebox.showerror("Erro", "Por favor, insira uma API Key válida.")
            return

        try:
            # Configura o cliente da API
            client = texttospeech.TextToSpeechClient()

            # Faz uma requisição para listar as vozes disponíveis
            voices = client.list_voices()

            # Filtra as vozes para incluir apenas as vozes Wavenet em inglês
            self.voices = [
                f"{voice.ssml_gender.name} - {voice.name}"
                for voice in voices.voices
                if "en-US" in voice.language_codes and "Wavenet" in voice.name
            ]

            # Atualiza o Combobox com as vozes disponíveis
            self.voice_selection["values"] = self.voices
            if self.voices:
                self.voice_selection.current(0)
            else:
                messagebox.showwarning("Aviso", "Nenhuma voz Wavenet em inglês encontrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar vozes: {str(e)}")

    def synthesize_speech(self, text, voice, speed):
        """Sintetiza o texto em áudio usando a API do Google Cloud Text-to-Speech."""
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice_params = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name=voice,
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE if "Female" in voice else texttospeech.SsmlVoiceGender.MALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=speed
        )
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice_params,
            audio_config=audio_config
        )
        return response.audio_content

    def play_audio(self, file):
        """Reproduz o áudio gerado."""
        try:
            playsound(file)  # Usando playsound para reprodução de áudio
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao reproduzir o áudio: {str(e)}")

    def test_audio(self):
        """Testa o áudio gerado a partir do texto inserido."""
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Erro", "Por favor, insira um texto para testar.")
            return

        api_key = self.api_key_entry.get().strip()
        if not api_key:
            messagebox.showerror("Erro", "Por favor, insira uma API Key válida.")
            return

        voice = self.voice_selection.get().split(" - ")[1]
        speed = self.speed_scale.get()

        try:
            audio_content = self.synthesize_speech(text, voice, speed)
            test_file = "test_output.mp3"
            with open(test_file, "wb") as out:
                out.write(audio_content)
            self.play_audio(test_file)
            os.remove(test_file)  # Excluir o arquivo após a reprodução
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao sintetizar ou reproduzir o áudio: {str(e)}")

    def convert_text(self):
        """Converte o texto em áudio e salva o arquivo."""
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Erro", "Por favor, insira um texto para conversão.")
            return

        api_key = self.api_key_entry.get().strip()
        if not api_key:
            messagebox.showerror("Erro", "Por favor, insira uma API Key válida.")
            return

        voice = self.voice_selection.get().split(" - ")[1]
        speed = self.speed_scale.get()

        try:
            audio_content = self.synthesize_speech(text, voice, speed)
            self.audio_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
            if self.audio_file:
                with open(self.audio_file, "wb") as out:
                    out.write(audio_content)
                self.play_audio(self.audio_file)
                messagebox.showinfo("Sucesso", "Texto convertido e salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao sintetizar ou salvar o áudio: {str(e)}")

    def download_audio(self):
        """Informa ao usuário que o áudio já foi salvo durante a conversão."""
        if not self.audio_file:
            messagebox.showerror("Erro", "Nenhum áudio foi gerado ainda.")
            return
        messagebox.showinfo("Sucesso", "Áudio já foi salvo durante a conversão.")


if __name__ == "__main__":
    root = tb.Window(themename="darkly")  # Janela com tema escuro
    app = TextToSpeechApp(root)
    root.mainloop()