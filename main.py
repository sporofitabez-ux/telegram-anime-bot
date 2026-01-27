import os
import re
import requests
import aiofiles
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

app = Client(
    "anime_downloader",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def is_nyaa(url: str):
    return "nyaa.si" in url

def extract_torrent(url: str):
    r = requests.get(url)
    match = re.search(r'href="(/download/\\d+\\.torrent)"', r.text)
    if not match:
        return None
    return "https://nyaa.si" + match.group(1)

async def download_file(url: str, filename: str):
    async with aiofiles.open(filename, "wb") as f:
        r = requests.get(url, stream=True)
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                await f.write(chunk)

@app.on_message(filters.command("start") & filters.group)
async def start(_, msg: Message):
    await msg.reply(
        "🤖 **Anime Downloader Userbot**\n\n"
        "📥 Use:\n"
        "`/baixar LINK`\n\n"
        "✅ Suporte:\n"
        "• Links diretos\n"
        "• nyaa.si\n"
        "• .torrent\n"
    )

@app.on_message(filters.command("baixar") & filters.group)
async def baixar(_, msg: Message):
    if len(msg.command) < 2:
        await msg.reply("❌ Use: `/baixar LINK`")
        return

    url = msg.command[1]

    await msg.reply("⬇️ Iniciando download...")

    if is_nyaa(url):
        torrent_url = extract_torrent(url)
        if not torrent_url:
            await msg.reply("❌ Não consegui extrair o torrent do nyaa")
            return
        url = torrent_url

    filename = os.path.join(DOWNLOAD_DIR, url.split("/")[-1])

    try:
        await download_file(url, filename)
        await msg.reply_document(filename)
        os.remove(filename)
    except Exception as e:
        await msg.reply(f"❌ Erro:\n`{e}`")

print("✅ Userbot iniciado com sucesso")
app.run()
