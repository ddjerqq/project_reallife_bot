import os
import discord
from discord.ext import commands
# from discord.ext.commands import Context as Ctx

from dotenv import load_dotenv

from src.client import Client
from src.view import PersistentView

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        welcome = next((
            channel
            for channel in guild.text_channels
            if "welcome" in channel.name.lower()
        ), None)
        if welcome is not None:
            client.welcome_channels[guild.id] = welcome

        rules = next((
            channel
            for channel in guild.text_channels
            if "rules" in channel.name.lower()
        ), None)
        if rules is not None:
            client.rule_channels[guild.id] = rules


@client.event
async def on_member_join(member: discord.Member):
    if (welcome := client.welcome_channels.get(member.guild.id)) is None:
        return

    rules = client.rule_channels.get(member.guild.id)
    rules = rules.mention if rules is not None else "წესების არხში"

    em = discord.Embed(
        title="ახალი წევრი!",
        description="**{}** შემოუერთდა ჩვენს სერვერს!\n\n\n\n".format(member.name),
        color=0x2D60CC,
    )
    em.add_field(
        name="გაეცანით დისქორდის წესებს",
        value=rules,
    )

    em.set_thumbnail(url=member.avatar.url)

    await welcome.send(
        embed=em
    )


@client.command(name="verification")
@commands.has_permissions(administrator=True)
async def verification(ctx: commands.Context):
    """Starts a persistent view."""
    # In order for a persistent view to be listened to, it needs to be sent to an actual message.
    # Call this method once just to store it somewhere.
    # In a more complicated program you might fetch the message_id from a database for use later.
    # However, this is outside the scope of this simple example.

    em = discord.Embed(
        title="როლის მიღება",
        description="იმისათვის რომ გამოიყენოთ ჩვენი დისქორდ სერვერის სრული ფუნქციონალი, გაიარეთ ვერიფიკაცია.",
        color=0x2D60CC,
    )
    em.set_thumbnail(url="https://i.imgur.com/YctJGwP.png")

    await ctx.send(embed=em, view=PersistentView())


if __name__ == "__main__":
    client.run(TOKEN)
