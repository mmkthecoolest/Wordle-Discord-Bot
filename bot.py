import imp
import json
import requests
import discord
import os
import time
from datetime import date, timedelta
from discord.ext import tasks


client = discord.Client()
#channel_id_exists = False
#channel_id = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!wordle_setup'):
        await message.delete()
        await message.channel.send("Setting up...")
        channel_id = message.channel.id
        await wordle_guess(channel_id)


async def wordle_guess(channel_id):

    while True:
        message_channel = client.get_channel(channel_id)
        yesterday = date.today() - timedelta(days=1)

        year = yesterday.year
        month = yesterday.month
        day = yesterday.day

        word_guess = json.loads(requests.get(
            "https://najemi.cz/wordle_answers/api/?day={0}&month={1}&year={2}".format(day, month, year)).text)["word"]
        await message_channel.send("Word guess for " + yesterday.isoformat() + " : " + word_guess + '\nhttps://www.merriam-webster.com/dictionary/' + word_guess)

        time.sleep(3600*24)

client.run("TOKEN")
