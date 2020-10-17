import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(RenameGroup(bot))

class RenameGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rename(self, ctx):
        ctx.send("dd")
