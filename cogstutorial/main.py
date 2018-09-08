from discord.ext import commands
# esse é o import que você devera fazer aqui
# e nos outros arquivos

modulos = [
    "comandos.comando",
]
# comandos é o nome da pasta onde o arquivo comando vai estar
# mas se o arquivo estiver na msm pasta use "comando" 
# ao inves de "comandos.comando"
# caso queira adicionar mais arquivos coloque uma virgula a cada arquivo

# conexao com discord
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
# remover aquele help horroroso
bot.remove_command("help")


# evento quando estiver online
@bot.event
async def on_ready():
    print("O bot está online")


if __name__ == "__main__":
    # para cada arquivo na lista
    for extension in modulos:
        try:
            bot.load_extension(extension)
        except Exception as ir:
            exc = '{}.{}'.format(type(ir).__name__, ir)
            print('falha ao carregar extensoes {} . {}'.format(extension, ir))
            
bot.run('tokenzinho ¬¬')
