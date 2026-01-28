import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

app = Client(
    name="anime_userbot",
    session_string=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    await message.reply_text(
        "🤖 **Anime Downloader Userbot**\n\n"
        "✅ Funciona em grupos\n"
        "📦 Envia arquivos grandes\n"
        "⚡ Base pronta para animes\n\n"
        "Use /help para ver comandos"
    )

@app.on_message(filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply_text(
        "📌 **Comandos disponíveis**\n\n"
        "/start – iniciar o bot\n"
        "/help – ajuda\n"
        "/ping – testar se está online\n\n"
        "⚠️ Em breve: download de animes"
    )

@app.on_message(filters.command("ping"))
async def ping_cmd(client: Client, message: Message):
    await message.reply_text("🏓 Pong! Estou online 🚀")

if __name__ == "__main__":
    print("✅ Userbot iniciado...")
    app.run()
