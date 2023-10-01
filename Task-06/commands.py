import discord
from discord.ext import commands

# Define your intents
intents = discord.Intents.default()
intents.typing = False  # Disable typing event (optional)
intents.presences = False  # Disable presence event (optional)

# Initialize the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define a command
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot with the token you copied from the Developer Portal
bot.run('MTE1NDQ5MzEzNTk1OTg5NjEzNQ.GAsncv.-BedRIxoz8x3B-5fUgz_f4PH1jxCooS3ZcNGA4')
