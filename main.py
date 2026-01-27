import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from downloader import baixar
from config import API_ID, API_HASH

app = Client(
    "anime_userbot",
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start") & filters.group)
async def start(_, msg: Message):
    await msg.reply(
        "🤖 <b>Anime Downloader</b>\n\n"
        "Use:\n"
        "<code>/baixar LINK</code>\n\n"
        "Suporte:\n"
        "• Magnet\n"
        "• Torrent (nyaa.si)\n"
        "• Link direto"
    )

@app.on_message(filters.command("baixar") & filters.group)
async def baixar_cmd(_, msg: Message):
    if len(msg.command) < 2:
        await msg.reply("❌ Envie o link junto com o comando.")
        return

    link = msg.command[1]
    status = await msg.reply("⬇️ Baixando... aguarde.")

    try:
        download = baixar(link)

        while not download.is_complete:
            await asyncio.sleep(5)
            download = download.api.get_download(download.gid)

        arquivo = download.files[0].path

        await status.edit("📤 Enviando arquivo...")
        await msg.reply_document(arquivo, caption="✅ Download concluído")
        await status.delete()

    except Exception as e:
        await status.edit(f"❌ Erro:\n<code>{e}</code>")

print("✅ Userbot iniciado")
app.run() 
