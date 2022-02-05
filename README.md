# Wordle Solutions Discord Bot

Wordle Solutions Discord Bot is a bot that posts yesterday's Wordle solution. Wordle generates a new word every midnight, however, this depends on the local timezone. For example, people in Australia can get the new Wordle before people in the US.

My plan is to host this bot and start it late night at EST time, to guarantee that there is no cheating possible (the bot only posts the solution per 24 hours). The bot will look for yesterday's Wordle solution during late night EST time.

This repo contains the code for the bot to run. It has been written using `discord.py` and uses an API provided by [Martin Najemi](https://najemi.cz/) ([API Source](https://www.reddit.com/r/wordlegame/comments/siw7oa/answers_api/)).

## How to Set Up
⚠ PLEASE DO NOT ADD THE BOT YET AS I STILL NEED TO FIGURE OUT HOSTING ⚠

1. Copy and paste [this link](https://discord.com/api/oauth2/authorize?client_id=939247798195478588&permissions=75792&scope=bot) to a browser to add the bot into your server (you must have server managing permissions). All the permissions needed by this bot are necessary (except the message managing permission if you don't want the bot to delete messages).
2. Once the bot is added, type `!wordle_setup` in the channel you desire. BE CAREFUL NOT TO ADD IT IN THE WRONG CHANNEL, OTHERWISE YOU WILL NEED TO KICK THE BOT OUT SINCE I DO NOT KNOW HOW TO MAKE THE BOT LEAVE THROUGH CODE YET.