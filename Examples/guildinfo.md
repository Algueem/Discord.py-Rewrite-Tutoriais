# Exemplo básico de como fazer seu Guild/Server info
Para fazer esse comando será necessário ter uma instância de discord.Guild.([Doc](https://discordpy.readthedocs.io/en/latest/api.html#guild))
Você pode obtê-la de diversas formas
```python
guild = message.guild
```
```python
guild = client.get_guild(id)
```

Docs:
* [Message.Guild](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.guild)
* [Client.get_guild](https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.get_guild)

Com a instância obtida, basta usar os atributos da [documentação]((https://discordpy.readthedocs.io/en/latest/api.html#guild))
por exemplo
```python
guild.owner # Dono do servidor (Também é um discord.Member)
guild.name # Nome do servidor
guild.id # ID do servidor
guild.members # Membros do servidor (Lista)
```

Além dos citados, existem diversos outros atributos de informações da guilda, basta ler a 
documentação que poderá colocar muitas informações no seu comando
