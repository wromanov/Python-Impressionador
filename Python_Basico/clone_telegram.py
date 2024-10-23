from telethon import TelegramClient, errors

# Solicitar credenciais e informações do usuário
api_id = 959430
api_hash = '5ed65a83569af23899d0a44d9f0838c9'

source_channel = -1002109379377
destination_channel = -1002368271467

# Nome do arquivo da sessão
session_name = 'clone_telegram'

# Inicializando o cliente do Telethon
client = TelegramClient(session_name, api_id, api_hash)

async def clone_messages():
    async with client:
        try:
            # Validar se o canal de origem e de destino são acessíveis
            source = await client.get_entity(source_channel)
            destination = await client.get_entity(destination_channel)
        except errors.rpcerrorlist.ChannelInvalidError:
            print("Erro: Um dos canais fornecidos é inválido ou inacessível.")
            return
        except ValueError as e:
            print(f"Erro: Não foi possível encontrar a entidade correspondente ({e}). Verifique os canais fornecidos.")
            return

        print(f"Clonando mensagens de {source_channel} para {destination_channel}...")

        try:
            # Pegando todas as mensagens do canal de origem desde a primeira (reverse=True)
            async for message in client.iter_messages(source, reverse=True):
                # Verificando se a mensagem é de texto
                if message.text:
                    # Enviando a mensagem de texto para o canal de destino
                    await client.send_message(destination, message.text)

                # Se for uma mídia (fotos, vídeos, documentos, etc.)
                if message.media:
                    # Reenviando a mídia para o canal de destino
                    await client.send_file(destination, message.media)

                print(f"Mensagem {message.id} clonada.")

            print("Clonagem completa!")
        except Exception as e:
            print(f"Ocorreu um erro durante a clonagem: {e}")

# Rodando o cliente e chamando a função de clonagem
client.start()
client.loop.run_until_complete(clone_messages())