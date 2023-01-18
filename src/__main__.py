import os
import discord
# from discord.ext.commands import Context as Ctx

from dotenv import load_dotenv

from src.client import Client


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
        title="მოგესალმებით Project RealLife-ში",
        description="ეს არის სატესტო ტექსტი\n\n\n\n",
        color=0x2D60CC,
    )
    em.add_field(
        name="შექმნის თარიღი",
        value=f"{member.created_at.date()}",
    )
    em.add_field(
        name="გაეცანით წესებს",
        value=rules,
    )

    em.set_thumbnail(url=member.avatar.url)

    await welcome.send(
        f"{member.mention}",
        embed=em
    )

if __name__ == "__main__":
    client.run(TOKEN)
