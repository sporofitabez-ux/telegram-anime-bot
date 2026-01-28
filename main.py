import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

app = Client(
    "userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message):
    await message.reply(
        "🤖 Bot ativo no grupo!\n\n"
        "Envie um link (torrent ou direto) que eu baixo e envio aqui."
    )

@app.on_message(filters.private & filters.command("start"))
async def start_private(client, message):
    await message.reply(
        "🤖 Userbot online!\n\n"
        "Me adicione em um grupo e me dê permissão para enviar arquivos."
    )

print("✅ Userbot iniciado...")
app.run()
