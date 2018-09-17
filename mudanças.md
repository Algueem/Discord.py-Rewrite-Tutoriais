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
Async | Rewrite
--------|--------
client.send_message(destino, conteudo) | destino.send(conteúdo)
client.send_file(filename="nome.extensao") | destino.send(file=discord.File(filename="nome.extensao"))
client.send_message(destino, embed=variaveldoembed) | destino.send(embed=variaveldoembed)

Bom, pra quem nao sabe o que seria destino, é basicamente o lugar para onde a mensagem(ou arquivo/embed) vai enviar,
pode ser definido por:
1. message.channel - canal da mensagem/comando
2. message.author - author da mensagem/comando(mais especificamente no privado/DM)
3. client.get_channel(id) - canal definido por id

logo ficaria:
```python
canal = message.channel
canal.send(mensagem)
```
ou
```python
canal = message.author
canal.send(mensagem)
```
ou
```python
canal = client.get_channel(id)
canal.send(mensagem)
```
