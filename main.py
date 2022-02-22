import discord, asyncio, os # Discord
from dotenv import load_dotenv # Get .env
from discord.ext import commands 
from keep_alive import keep_alive # Server

from commands import example # Commands


prefix = "-"
cogs = [ example ]
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help') # Remove default help

for i in range(len(cogs)):
	cogs[i].setup(bot)


async def status_task():  # Activities
	while True:
		await bot.change_presence(activity=discord.Game(
			name="Yey"))
		await asyncio.sleep(10)

@bot.event  # Login
async def on_ready():
	print(f'\n{bot.user.name}')
	print("-> Logged successfully")
	bot.loop.create_task(status_task())  # Changing Activity


@bot.event # Message
async def on_message(message):
	if message.author == bot.user:
		return
		
	await bot.process_commands(message)


keep_alive()

load_dotenv(dotenv_path='.env') # Load .env
bot.run(os.getenv('TOKEN')) # Importing TOKEN from .env
