from __future__ import annotations

from typing import Any

import discord
from discord.ext import commands
from src.view import PersistentView


class Client(commands.Bot):
    def __init__(self, **options: Any):
        super().__init__(
            "!",
            intents=discord.Intents.all(),
            **options
        )
        self.welcome_channels: dict[int, discord.TextChannel] = {}
        self.rule_channels: dict[int, discord.TextChannel] = {}

    async def setup_hook(self) -> None:
        # Register the persistent view for listening here.
        # Note that this does not send the view to any message.
        # In order to do this you need to first send a message with the View, which is shown below.
        # If you have the message_id you can also pass it as a keyword argument, but for this example
        # we don't have one.
        self.add_view(PersistentView())
