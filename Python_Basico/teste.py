import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as tb
from gtts import gTTS
import os


class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Converter")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.style = tb.Style(theme="darkly")  # Aplicando o tema escuro

        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Entrada para a API Key
        ttk.Label(main_frame, text="API Key:").pack(anchor="w")
        self.api_key_entry = ttk.Entry(main_frame, width=50, show="*")
        self.api_key_entry.pack(pady=5, fill="x")

        # Caixa de texto
        ttk.Label(main_frame, text="Texto para conversão:").pack(anchor="w")
        self.text_entry = tk.Text(main_frame, height=5, wrap="word")
        self.text_entry.pack(pady=5, fill="x")

        # Escolher voz
        ttk.Label(main_frame, text="Escolher voz:").pack(anchor="w")
        self.voice_selection = ttk.Combobox(main_frame, values=["en-US-Wavenet-A", "en-US-Wavenet-B", "en-US-Wavenet-C",
                                                                "en-US-Wavenet-D", "en-US-Wavenet-E",
                                                                "en-US-Wavenet-F"], state="readonly")
        self.voice_selection.pack(pady=5, fill="x")
        self.voice_selection.current(0)

        # Ajustar velocidade
        ttk.Label(main_frame, text="Velocidade da voz:").pack(anchor="w")
        self.speed_scale = ttk.Scale(main_frame, from_=0.5, to=2.0, orient="horizontal")
        self.speed_scale.set(1.0)
        self.speed_scale.pack(pady=5, fill="x")

        # Botões
        self.convert_button = ttk.Button(main_frame, text="Converter", command=self.convert_text)
        self.convert_button.pack(pady=5, fill="x")

        self.download_button = ttk.Button(main_frame, text="Download Áudio", command=self.download_audio)
        self.download_button.pack(pady=5, fill="x")

        self.audio_file = None

    def convert_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Erro", "Por favor, insira um texto para conversão.")
            return

        voice = self.voice_selection.get()
        speed = self.speed_scale.get()

        tts = gTTS(text=text, lang='en', tld="com", slow=speed < 1.0)
        self.audio_file = "output.mp3"
        tts.save(self.audio_file)
        os.system(f"start {self.audio_file}")  # Reproduzir áudio automaticamente
        messagebox.showinfo("Sucesso", "Texto convertido e reproduzido com sucesso!")

    def download_audio(self):
        if not self.audio_file:
            messagebox.showerror("Erro", "Nenhum áudio foi gerado ainda.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if save_path:
            os.rename(self.audio_file, save_path)
            messagebox.showinfo("Sucesso", "Áudio salvo com sucesso!")


if __name__ == "__main__":
    root = tb.Window(themename="darkly")  # Janela com tema escuro
    app = TextToSpeechApp(root)
    root.mainloop()
