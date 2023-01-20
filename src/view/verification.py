from discord.ext import commands
import discord


# Define a simple View that persists between bot restarts
# In order for a view to persist between restarts it needs to meet the following conditions:
# 1) The timeout of the View has to be set to None
# 2) Every item in the View has to have a custom_id set
# It is recommended that the custom_id be sufficiently unique to
# prevent conflicts with other buttons the bot sends.
# For this example the custom_id is prefixed with the name of the bot.
# Note that custom_ids can only be up to 100 characters long.
class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ვერიფიკაცია", style=discord.ButtonStyle.green, custom_id="verification")
    async def green(self, inter: discord.Interaction, _button: discord.ui.Button):
        await inter.response.send_message("ვერიფიკაცია გავლილია", ephemeral=True)
        # member role is added here
        # this role is from project real life `Member` role
        role = inter.guild.get_role(738831368196456568)
        await inter.user.add_roles(role, atomic=True)
