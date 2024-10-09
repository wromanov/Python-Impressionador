import asyncio
import time
import json
from telethon import TelegramClient, errors

# Configurações de API do Telegram
api_id = 959430
api_hash = '5ed65a83569af23899d0a44d9f0838c9'

# IDs do canal de origem e destino
source_channel = -1002109379377
destination_channel = -1002368271467

# Caminho para o arquivo de checkpoint
CHECKPOINT_FILE = 'clone_checkpoint.json'
BATCH_SIZE = 100  # Número de mensagens por lote
CLONE_LIMIT = 1000  # Máximo de mensagens clonadas por período de 6 horas
CLONE_INTERVAL = 10  # Intervalo entre lotes (em segundos)
PAUSE_DURATION = 6 * 3600  # 6 horas em segundos

# Nome do arquivo da sessão
session_name = 'clone_telegram'

# Inicializando o cliente do Telethon
client = TelegramClient(session_name, api_id, api_hash)

def load_checkpoint():
    """Carrega o último offset (mensagem clonada) e o contador de mensagens do arquivo."""
    try:
        with open(CHECKPOINT_FILE, 'r') as file:
            data = json.load(file)
            return data.get('offset', 0), data.get('cloned_count', 0)
    except FileNotFoundError:
        return 0, 0  # Se não existir o arquivo, começamos do zero

def save_checkpoint(offset, cloned_count):
    """Salva o offset atual e o contador de mensagens clonadas."""
    with open(CHECKPOINT_FILE, 'w') as file:
        json.dump({'offset': offset, 'cloned_count': cloned_count}, file)

def countdown_timer(seconds):
    """Mostra uma contagem regressiva do tempo de pausa."""
    while seconds > 0:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        time_left = f'{h:02d}:{m:02d}:{s:02d}'
        print(f"Pausa... Tempo restante: {time_left}", end='\r')
        time.sleep(1)
        seconds -= 1

async def clone_messages():
    offset, cloned_count = load_checkpoint()  # Carregar o estado atual

    while cloned_count < CLONE_LIMIT:
        try:
            # Pegar mensagens desde a mais antiga (reverse=True)
            async for message in client.iter_messages(source_channel, reverse=True, offset_id=offset, limit=BATCH_SIZE):
                # Clonar mensagens de texto
                if message.text:
                    await client.send_message(destination_channel, message.text)
                # Clonar arquivos de mídia
                if message.media:
                    await client.send_file(destination_channel, message.media)

                print(f"Mensagem {message.id} clonada.")
                offset = message.id  # Atualizar o offset para a próxima mensagem
                cloned_count += 1

                if cloned_count >= CLONE_LIMIT:
                    print(f"Limite de {CLONE_LIMIT} mensagens atingido. Pausando por 6 horas...")
                    save_checkpoint(offset, cloned_count)  # Salvar o estado
                    countdown_timer(PAUSE_DURATION)  # Contagem regressiva de 6 horas
                    cloned_count = 0  # Reinicia o contador para a próxima sessão
                    break

            save_checkpoint(offset, cloned_count)  # Salvar o estado após o lote
            await asyncio.sleep(CLONE_INTERVAL)  # Aguardar 10 segundos antes de clonar o próximo lote

        except errors.FloodWaitError as e:
            print(f"Excesso de requisições: aguardando {e.seconds} segundos.")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break

    # Espera 6 horas para reiniciar o processo de clonagem
    countdown_timer(PAUSE_DURATION)  # Contagem regressiva de 6 horas
    await clone_messages()  # Reiniciar automaticamente

async def main():
    # Inicia o processo de clonagem
    await client.start()
    await clone_messages()

# Executa o cliente do Telegram e o processo de clonagem
if __name__ == '__main__':
    client.loop.run_until_complete(main())
