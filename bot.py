import discord
from googletrans import Translator
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
translator = Translator()

@client.event
async def on_ready():
    print(f"Inloggad som {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content

    # Reagera endast om meddelandet börjar med "translate "
    if not content.lower().startswith("translate "):
        return

    # Ta bort ordet "translate"
    swedish_text = content[len("translate "):].strip()

    if not swedish_text:
        await message.channel.send("❌ Skriv text efter `translate`")
        return

    try:
        result = translator.translate(
            swedish_text,
            src="sv",
            dest="en"
        )

        await message.channel.send(
            f"🇸🇪 → 🇬🇧\n{result.text}"
        )

    except Exception as e:
        await message.channel.send("❌ Kunde inte översätta texten")

# DISCORD TOKEN från Render Environment Variable
client.run(os.environ["DISCORD_TOKEN"])
