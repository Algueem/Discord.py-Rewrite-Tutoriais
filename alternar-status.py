# bom para o bot ficar trocando de status devemos
# fazer os imports primeiramente
import discord
import asyncio

# vamos fazer a conexao com o discord
client = discord.Client()

# logo após vamos criar um evento para quando o bot estiver online
@client.event
async def on_ready()
    print("Eu estou online")
    # ele vai imprimir isso no console, se aparecer essa mensagem ele está online
    while True:
        # quando estiver online...
        await client.change_presence(activity=discord.Game(name="Nome do seu jogo"))
        await asyncio.sleep(60)
        # vai esperar 60 segundos
        await client.change_presence(activity=discord.Game(name="Nome do seu jogo 2"))
        # vai alterar depois de 60 segundos para a 2 presence
        await asyncio.sleep(60)
        # bom, aqui não vai alterar mais nenhum status, mas por causa do while True
        # vai alterar para o primeiro status repetindo o ciclo infinitamente
        
        
client.run('token aqui')
