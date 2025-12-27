import discord
import os
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # ignorera bottar
    if message.author.bot:
        return

    content = message.content

    # ska BARA trigga om man börjar med "translate "
    if not content.lower().startswith("translate "):
        return

    text_to_translate = content[len("translate "):].strip()
    if not text_to_translate:
        return

    try:
        translated = translator.translate(
            text_to_translate,
            src="sv",
            dest="en"
        ).text

        # redigera användarens meddelande
        await message.edit(
            content=f"🇸🇪 {text_to_translate}\n🇬🇧 {translated}"
        )

    except Exception as e:
        print("Translation error:", e)

bot.run(os.getenv("DISCORD_TOKEN"))
