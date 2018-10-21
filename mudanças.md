# Mudanças do discord.py async para a rewrite

## Geral
Async | Rewrite
--------|--------
server | guild
client.get_channel("id") | client.get_channel(id)

Sim agora o id não é mais string(uma variavel de texto definida por ' ou ")
agora é int(numero inteiro) logo quando for usar uma variavel de texto e for usar em algo q seja id converta em int 
usando int("12313") que ficará 12313(so n coloque letras como "abcd" claro).


## Client e on_message
### Envio de mensagens/arquivos/embeds
Async | Rewrite
--------|--------
client.send_message(destino, conteudo) | destino.send(conteúdo)
client.send_file(filename="nome.extensao") | destino.send(file=discord.File(filename="nome.extensao"))
client.send_message(destino, embed=variaveldoembed) | destino.send(embed=variaveldoembed)

Bom, pra quem nao sabe o que seria destino, é basicamente o lugar para onde a mensagem(ou arquivo/embed) vai enviar,
pode ser definido por:
1. message.channel - canal da mensagem/comando
2. message.author - autor da mensagem/comando(mais especificamente no privado/DM)
3. client.get_channel(id) - canal definido por id

logo ficaria:
```python
destino = message.channel
destino.send(mensagem)
```
ou
```python
destino = message.author
destino.send(mensagem)
```
ou
```python
destino = client.get_channel(id)
destino.send(mensagem)
```

### Editando mensagens/embed do bot e deletando mensagens de usuarios
Async | Rewrite
--------|--------
client.delete_message(message) | message.delete()
client.delete_message(todelete) | todelete.delete()
client.edit_message(antes, embed/content="") | antes.edit(embed/content="")

Em relação a editar/deletar mensagens é bem simples, para deletar a mensagem do autor do comando seria:
```python
# message é a mensagem do usuario
message.delete()
```
para deletar a que o bot mandar ficaria:
```python
variavelqualquer = await message.channel.send("Olá")
variavelqualquer.delete()
```

bom, como não tem como editar de outra pessoa, para editar a do bot ficaria:
```python
variavelqualquer = await message.channel.send("Olá")
variavelqualquer.edit(content="Oi")
```
porém, se for um embed é diferente, ficaria:
```python
embed = discord.Embed(title="Oi")
variavelqualquer = await message.channel.send(embed=embed)
embed2 = discord.Embed(title="Olá")
variavelqualquer.edit(embed=embed2)
```
