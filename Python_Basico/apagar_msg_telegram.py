from telethon import TelegramClient, errors
import asyncio

# Solicitar credenciais e informações do usuário
api_id = 959430
api_hash = '5ed65a83569af23899d0a44d9f0838c9'

channel = 7935552752

# Nome da sessão
session_name = 'delete_channel_messages'

# Inicializando o cliente do Telethon
client = TelegramClient(session_name, api_id, api_hash)

async def delete_messages():
    async with client:
        try:
            # Validar se o canal fornecido é acessível e se você tem permissão para deletar mensagens
            entity = await client.get_entity(channel)
        except errors.rpcerrorlist.ChannelInvalidError:
            print("Erro: O canal fornecido é inválido ou inacessível.")
            return
        except ValueError as e:
            print(f"Erro: Não foi possível encontrar a entidade correspondente ({e}). Verifique o canal fornecido.")
            return

        print(f"Apagando todas as mensagens do canal {channel}...")

        try:
            # Iterar sobre todas as mensagens do canal
            async for message in client.iter_messages(entity):
                if message:
                    # Apagar cada mensagem
                    await client.delete_messages(entity, message.id)
                    print(f"Mensagem {message.id} apagada.")

            print(f"Todas as mensagens do canal {channel} foram apagadas.")
        except Exception as e:
            print(f"Ocorreu um erro durante a exclusão das mensagens: {e}")

# Rodando o cliente e chamando a função de deleção
client.start()
client.loop.run_until_complete(delete_messages())