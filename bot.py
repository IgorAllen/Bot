import random
import discord
from discord.ext import commands

# Bot configuration
TOKEN = 'Datum'  # Replace with your bot's token
PREFIX = '!'  # Prefix for bot commands

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

# Event to indicate that the bot is online
@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and ready to roll dice!")

# Command to roll dice
@bot.command(name='roll')
async def roll_dice(ctx, dice_type: str):
    try:
        # Check if the format is correct (e.g., 1d20, 2d6)
        quantity, faces = map(int, dice_type.lower().split('d'))
        
        if quantity <= 0 or faces <= 0:
            await ctx.send("Please enter positive values for quantity and faces of the dice.")
            return

        # Roll the dice and calculate the total
        results = [random.randint(1, faces) for _ in range(quantity)]
        total = sum(results)

        # Send the result in the chat
        await ctx.send(f"🎲 Rolling {quantity}d{faces}: {results} \nTotal: {total}")

    except ValueError:
        await ctx.send("Invalid format! Use the format 'XdY', where X is the quantity of dice and Y is the number of faces (e.g., 1d20, 2d6).")

# Run the bot
bot.run(TOKEN)
