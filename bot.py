import json
from nextcord.ext import commands
from cogs_loader import load_cog_list

with open('config.json') as json_file:
    config = json.load(json_file)

token = config['token']

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


for py_file in load_cog_list():
    bot.load_extension(py_file)

bot.run(token)
