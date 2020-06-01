import os
import csv
import requests
import pandas as pd
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '>', case_insensitive=True)
bot.remove_command('help')
TOKEN = ''

@bot.event
async def on_ready():
    print('Bot Activated!')

#help command
@bot.command(aliases=['h'])
async def help(ctx):
    await ctx.send("""```
    Commands: 1.
    !mine [ore][mass][percent]```""")

#Mining Calculator Star Citizen
@bot.command(aliases=['m'])
async def mine(ctx, mineral, arg1: float, arg2: float):
    mData = pd.read_csv('prices.csv')
    for each in mData.iterrows():
        if each[1]['mineral'] == mineral or each[1]['alias1'] == mineral or each[1]['alias2'] == mineral:
            price = each[1]['price']
            rmass = arg1
            composition = arg2
            mass = (arg2 * arg1) / 100
            units = mass * 2
            estimation = units * price
            value = round(estimation, 2)

            cmos = str(arg2) + '%'
            embed = discord.Embed(title=each[1]['mineral'], colour = discord.Colour.blue())
            embed.add_field(name='Mass', value=rmass, inline=True)
            embed.add_field(name='Composition', value=cmos, inline=True)
            embed.add_field(name='Value', value=value, inline=False)
            await ctx.send(embed=embed)
            break

bot.run(TOKEN)
