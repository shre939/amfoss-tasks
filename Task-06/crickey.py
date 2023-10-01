import discord
from discord.ext import commands

# Initialize the bot
bot = commands.Bot(command_prefix='!')

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
