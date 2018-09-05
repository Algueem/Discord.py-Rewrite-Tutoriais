from discord.ext import commands
# o import que deverá ter em todos os arquivos

# nessa "AlgumaClasse" vc pode colocar qualquer coisa
class AlgumaClasse:
    def __init__(self, bot)
        self.bot = bot
        
    @commands.command()
    # até aqui você deverá fazer igual em todos os comandos
    async def nomedocomando(self, ctx):
        # no "nomedocomando" coloque o comando
        
        # enviar a mensagem
        # ctx.send na rewrite vai responder para o canal da mensagem
        await ctx.send("test cogs")
        
        
# essa parte também deverá colocar em todos os arquivos
def setup(bot):
    # o nome da classe emcima deverá colocar abaixo
    bot.add_cog(AlgumaClasse(bot))
    # colocar um print para saber se foi carregado
    print('comando carregado')
    # depois execute o arquivo main e teste o comando e veja se irá responder
    # se nao respondeu deve ter feito algo errado
