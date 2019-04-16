# Como usar argumentos com Discord.py

```python
@bot.command()
async def example1(arg1, arg2, *args):
    ...

# Usando "?example1 um dois três quatro" vamos ter
# arg1 = 'um'
# arg2 = 'dois'
# args = ('três', 'quatro')

@bot.command()
async def example2(arg1, arg2, *, args):
    ...

# Usando "?example2 um dois três quatro" vamos ter
# arg1 = 'um'
# arg2 = 'dois'
# args = 'três quatro'
```
