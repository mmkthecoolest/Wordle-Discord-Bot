from nextcord.ext import commands
from cogs_loader import load_cog_list


class OwnerCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="reload")
    async def reload_command(self, ctx: commands.Context):
        file_list = ctx.message.content.split(" ")[1:]
        cogs_list = load_cog_list()
        for file in file_list:
            if file not in cogs_list:
                await ctx.send("One or more parameters does not exist as a cog file, please try again")
                return

        for file in file_list:
            print("reloading extension " + file + ".py")
            await ctx.send("reloading extension " + file + ".py")
            self.bot.reload_extension(file)


def setup(bot: commands.Bot):
    bot.add_cog(OwnerCommands(bot))
