import discord
from discord.ext import commands

class example(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx): # Name and parameters
		msg = await ctx.reply('Pong!')
		await msg.add_reaction('🏓')

def setup(bot):
  bot.add_cog(example(bot)) # "Exporting"