import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def issue(ctx):
    facts = ['5 июля ежегодно отмечается Всемирный день окружающей среды.', 
            'В условиях загрязнения птицы поют мелодичнее', 
            'В будущем мы сможем выбрасывать мусор на солнце']
    fact = (random.choice(facts))
    await ctx.send(fact)

@bot.command()
async def envihelp(ctx):
    advices = ['Повторно использовать вещи', 
               'Использовать концентрированные продукты', 
               'жертвовать неиспользуемыми вещами']
    advice = (random.choice(advices))
    await ctx.send(advice)

@bot.command()
async def help_env(ctx):
    actions = ['Выключи свет!', 
               'У тебя много бутылок? Сходи сдай их!', 
               'Не расходуй воду!']
    action = (random.choice(actions))
    await ctx.send(action)


bot.run('TOKEN')
