import os
import asyncio
import aiohttp
import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

app = Client(
    "userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# ─────────────────────────────
# /start
# ─────────────────────────────
@app.on_message(filters.command("start") & filters.group)
async def start(_, msg: Message):
    await msg.reply(
        "🤖 **Bot ativo no grupo!**\n\n"
        "📥 `/download <url>` → download direto\n"
        "🧲 `/torrent <magnet>` → torrent\n",
        quote=True
    )

# ─────────────────────────────
# DOWNLOAD DIRETO
# ─────────────────────────────
@app.on_message(filters.command("download") & filters.group)
async def direct_download(_, msg: Message):
    if len(msg.command) < 2:
        await msg.reply("❌ Use: `/download <url>`")
        return

    url = msg.command[1]
    filename = os.path.join(DOWNLOAD_DIR, url.split("/")[-1])

    status = await msg.reply("⬇️ Baixando arquivo...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    await status.edit("❌ Erro ao baixar o arquivo.")
                    return

                with open(filename, "wb") as f:
                    while True:
                        chunk = await resp.content.read(1024 * 1024)
                        if not chunk:
                            break
                        f.write(chunk)

        await status.edit("📤 Enviando arquivo...")
        await msg.reply_document(filename)

    except Exception as e:
        await status.edit(f"❌ Erro: `{e}`")

    finally:
        if os.path.exists(filename):
            os.remove(filename)

# ─────────────────────────────
# TORRENT / MAGNET
# ─────────────────────────────
@app.on_message(filters.command("torrent") & filters.group)
async def torrent_download(_, msg: Message):
    if len(msg.command) < 2:
        await msg.reply("❌ Use: `/torrent <magnet ou link .torrent>`")
        return

    magnet = msg.command[1]
    status = await msg.reply("🧲 Iniciando torrent...")

    try:
        process = await asyncio.create_subprocess_exec(
            "aria2c",
            magnet,
            "--dir", DOWNLOAD_DIR,
            "--seed-time=0",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        await process.communicate()

        files = os.listdir(DOWNLOAD_DIR)
        if not files:
            await status.edit("❌ Torrent não gerou arquivos.")
            return

        await status.edit("📤 Enviando arquivos...")
        for file in files:
            path = os.path.join(DOWNLOAD_DIR, file)
            await msg.reply_document(path)
            os.remove(path)

    except Exception as e:
        await status.edit(f"❌ Erro: `{e}`")

# ─────────────────────────────
app.run()
