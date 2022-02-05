import json
import requests
import nextcord
import os
from datetime import date, timedelta
from nextcord.ext import tasks, commands

from dotenv import load_dotenv

load_dotenv()


class MyClient(nextcord.Client):
    channel_id = []
    channel_id_exists = False

    async def on_ready(self):
        print(f'We have logged in as {self}')

    bot = commands.Bot(command_prefix="!", intents= nextcord.Intents.default())
    
    @bot.command(name="wordle_setup")
    async def wordle_setup(self, ctx):
        await ctx.message.delete()
        await ctx.send("Setting up...")
        self.channel_id.append(ctx.message.channel.id)
        self.channel_id_exists = True

    @tasks.loop(seconds=86400)
    async def wordle_guess(self):
        if self.channel_id_exists:

            yesterday = date.today() - timedelta(days=1)

            year = yesterday.year
            month = yesterday.month
            day = yesterday.day

            for channel_id_iter in self.channel_id:
                message_channel = self.get_channel(channel_id_iter)
                word_guess = json.loads(requests.get(
                    "https://najemi.cz/wordle_answers/api/?day={0}&month={1}&year={2}".format(day, month, year)).text)["word"]
                await message_channel.send("Wordle guess for " + yesterday.isoformat() + " : " + word_guess + '\nhttps://www.merriam-webster.com/dictionary/' + word_guess)

client = MyClient()
client.wordle_guess.start()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
