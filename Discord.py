# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m gonna put some dirt in your eye',
        (
            'You want forgiveness? Get religion.'
        ),
        (
            'How the fuck are ye?'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name = 'cat')
async def dog(ctx):
    await ctx.send(file=discord.File('download.png'))
bot.run(TOKEN)