import discord
from discord import app_commands
from discord.ext import commands

class LinkButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label='Vote me!', style=discord.ButtonStyle.link, url="https://top.gg/bot/1088961569431502932")

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.defer()

class InviteView(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(LinkButton())

class VoteCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="vote", description="Use this to vote our bot on top.gg!")
    async def vote(self, interaction: discord.Interaction):
        await interaction.response.defer()

        try:
            embed = discord.Embed(title=f"Vote for TarnishedSouls",
                                  description=f"Thanks! You can vote the bot with the button below \nand you can also write a review! 💕\n"
                                              f"Thanks")

            await interaction.followup.send(embed=embed, view=InviteView())
        except Exception as e:
            await self.client.send_error_message(e)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(VoteCommand(client))
