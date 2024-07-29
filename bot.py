from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
GENERAL_CHANNEL_ID = int(os.getenv("GENERAL_CHANNEL_ID"))
FARM_CHANNEL_ID = int(os.getenv("FARM_CHANNEL_ID"))
JOJO_ID = int(os.getenv("JOJO_ID"))
HAYDN_ID = int(os.getenv("HAYDN_ID"))

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

farm_emoji_dict = {
    "farm": "🚜",
    "goat": "🐐",
    "goats": "🐐",
    "cow": "🐄",
    "cows": "🐄",
    "chicken": "🐓",
    "chickens": "🐓",
    "farmer": "👨‍🌾",
    "sun": "☀️",
    "bird": "🐦",
    "birds": "🐦",
    "carrot": "🥕",
    "carrots": "🥕",
    "wheat": "🌾",
    "cake": "🍰",
    "dairy": "🥛",
    "milk": "🥛",
    "recipe": "📜",
    "day": "🌞",
    "train": "🚂",
    "harvest": "🌾",
    "cheese": "🧀",
    "butter": "🧈",
    "egg": "🥚",
    "eggs": "🥚",
    "sugarcane": "🎋",
    "barbecue": "🍖",
    "earth": "🌍",
    "harvest": "🌾",
    "outhouse": "🏠",
}


@bot.event
async def on_ready():
    print(f"Ready... logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Successfully synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.event
async def on_message(message):
    if message.author.id == HAYDN_ID and message.channel.id == GENERAL_CHANNEL_ID:
        await message.channel.send(
            """
            Harlem is a focal point of the origins of the entire jazz genre.
            Its cultural contribution is unmatched and truly makes the location
            an oasis, dare I say Valhalla, of the modern era
            """
        )

    if (
        message.author.id == JOJO_ID
        and message.channel.id == FARM_CHANNEL_ID
        and not message.attachments
    ):
        # reacts with "I" "L" "Y" "heart emoji" to every message
        await message.add_reaction("🇮")
        await message.add_reaction("🇱")
        await message.add_reaction("🇾")
        await message.add_reaction("❤️")
        for word in message.content.split():
            word = word.lower()
            if word in farm_emoji_dict:
                await message.add_reaction(farm_emoji_dict[word])

    await bot.process_commands(message)


@bot.tree.command(name="purge", description="Delete the last 10 messages")
async def purge(interaction: discord.Interaction):
    deleted = await interaction.channel.purge(limit=10)
    await interaction.channel.send(f"Deleted {len(deleted)} messages.")


bot.run(BOT_TOKEN)
