import os
import telebot
from telebot.types import Message
from downloader import aria2_add

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN não definido nas variáveis de ambiente")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(msg: Message):
    bot.reply_to(
        msg,
        "🤖 <b>Anime Downloader Bot</b>\n\n"
        "Use o comando:\n"
        "<code>/download LINK</code>\n\n"
        "✅ Funciona em grupos\n"
        "✅ Suporte a magnet\n"
        "✅ Suporte a nyaa.si\n"
    )

@bot.message_handler(commands=["download"])
def download(msg: Message):
    try:
        parts = msg.text.split(maxsplit=1)

        if len(parts) < 2:
            bot.reply_to(
                msg,
                "❌ Envie o link junto com o comando\n"
                "Exemplo:\n<code>/download LINK</code>"
            )
            return

        link = parts[1].strip()

        result = aria2_add(link)

        if "result" in result:
            bot.reply_to(
                msg,
                "⬇️ <b>Download iniciado com sucesso!</b>\n"
                "⏳ Aguarde o processamento."
            )
        else:
            bot.reply_to(
                msg,
                f"❌ Erro ao iniciar download:\n<code>{result}</code>"
            )

    except Exception as e:
        bot.reply_to(msg, f"❌ Erro interno:\n<code>{e}</code>")

print("🤖 Bot iniciado com sucesso")
bot.infinity_polling(skip_pending=True)
