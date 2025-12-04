import os

import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        await self.change_presence(status=discord.Status.dnd)

    async def load_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                await self.load_extension(f"bot.cogs.{filename[:-3]}")
