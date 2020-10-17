import discord
from discord.ext import commands

import uuid

import json_manager
import database_manager
import group

def setup(bot):
    bot.add_cog(CreateGroup(bot))

class CreateGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx, arg1):
        #print(group.Group(uuid.uuid4, arg1, {"leader": ctx.author}, json_manager.curent_file("./json/default.json")).to_string())
        database_manager.add_group(group.Group(uuid.uuid4(), arg1, {"leader": ctx.author.id}, json_manager.curent_file("./json/default.json")))
        await ctx.send("group create {}".format(arg1))