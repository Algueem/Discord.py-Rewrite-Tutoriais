# Como alterar o status do seu bot(rewrite)

Primeiramente vou mostrar o que deve ter para alterar o status

```py
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Bot Online")
    # Aqui vai ficar a parte do change_presence, ele irá variar de acordo com o status(transmitindo, jogando, assistindo, ouvindo)
    
client.run('token aqui')
```

## Jogando

```py
await client.change_presence(activity=discord.Activity(name="um jogo", type=discord.ActivityType.playing))
```

## Assistindo
```py
await client.change_presence(activity=discord.Activity(name="um programa", type=discord.ActivityType.watching))
```

## Ouvindo
```py
await client.change_presence(activity=discord.Activity(name="um cantor", type=discord.ActivityType.listening))
```

## Transmitindo
```py
await client.change_presence(activity=discord.Streaming(name="ao vivo", url="https://twitch.tv/"))
```
