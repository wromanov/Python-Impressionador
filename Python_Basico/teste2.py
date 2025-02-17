from google.cloud import texttospeech

def text_to_speech_test():
    # Configure o cliente da API
    client = texttospeech.TextToSpeechClient()

    # Texto de entrada para conversão
    text_input = texttospeech.SynthesisInput(text="Olá! Este é um teste da API Google Text-to-Speech.")

    # Configuração da voz
    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-BR",  # Idioma e região
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL  # Gênero da voz
    )

    # Configuração do áudio
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # Formato de saída
    )

    # Solicitação de síntese
    response = client.synthesize_speech(input=text_input, voice=voice, audio_config=audio_config)

    # Salvar o áudio em um arquivo
    with open("output.mp3", "wb") as audio_file:
        audio_file.write(response.audio_content)
    print("Áudio gerado e salvo como 'output.mp3'.")

# Executa a função de teste
if __name__ == "__main__":
    text_to_speech_test()
