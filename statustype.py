# como alterar o status para seu bot (transmitindo, jogando, assistindo, ouvindo)
import discord

client = discord.Client()

# type 1 = jogando
# type 2 = ouvindo
# type 3 = assistindo

@client.event
async def on_ready():
    print("Bot Online")
    # diferente do outro tutorial, esse vai ficar so um status
    # mas se quiser ficar alternando faça o outro tutorial e altere o change presence
    await client.change_presence(activity=discord.Activity(name="Nome do jogo", type=3))
    
client.run('token aqui')
