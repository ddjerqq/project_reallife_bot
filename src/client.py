from __future__ import annotations

from typing import Any

import discord
from discord.ext import commands


class Client(commands.Bot):
    def __init__(self, **options: Any):
        super().__init__(
            "!",
            intents=discord.Intents.all(),
            **options
        )
        self.welcome_channels: dict[int, discord.TextChannel] = {}
        self.rule_channels: dict[int, discord.TextChannel] = {}
