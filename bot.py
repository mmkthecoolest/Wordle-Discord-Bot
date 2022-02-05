import nextcord
import asyncio
import json
import requests
import os
from datetime import date, timedelta
from nextcord.ext import tasks, commands

bot = commands.Bot(command_prefix='!')

with open('config.json') as f:
    config = json.load(f)

token = config['token']

channel_id = []
channel_id_exists = False

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name="wordle_setup")
async def wordle_setup(ctx):
    await ctx.message.delete()
    await ctx.send("Setting up...")
    channel_id.append(ctx.message.channel.id)
    channel_id_exists = True
    while True:
        if channel_id_exists:
            yesterday = date.today() - timedelta(days=1)

            year = yesterday.year
            month = yesterday.month
            day = yesterday.day

            for channel_id_iter in channel_id:
                message_channel = bot.get_channel(channel_id_iter)
                word_guess = json.loads(requests.get(
                    "https://najemi.cz/wordle_answers/api/?day={0}&month={1}&year={2}".format(day, month, year)).text)["word"]
                await message_channel.send("Wordle guess for " + yesterday.isoformat() + " : " + word_guess + '\nhttps://www.merriam-webster.com/dictionary/' + word_guess)

        await asyncio.sleep(86400)

bot.run(token)
