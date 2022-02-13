from nextcord.ext import commands
from datetime import date, timedelta
import asyncio
#import json
#import requests


class WordleCommands(commands.Cog):
    channel_id = []
    channel_id_exists = False

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="wordle_setup")
    async def wordle_setup(self, ctx):
        await ctx.message.delete()
        await ctx.send("Setting up...")
        self.channel_id.append(ctx.message.channel.id)
        self.channel_id_exists = True
        if self.channel_id_exists:
            yesterday = date.today() - timedelta(days=1)

            year = yesterday.year
            month = yesterday.month
            day = yesterday.day

            for channel_id_iter in self.channel_id:
                message_channel = self.bot.get_channel(channel_id_iter)
                word_guess = "pleat"
                await message_channel.send("Wordle guess for " + yesterday.isoformat() + " : " + word_guess + '\nhttps://www.merriam-webster.com/dictionary/' + word_guess)


def setup(bot: commands.Bot):
    bot.add_cog(WordleCommands(bot))
