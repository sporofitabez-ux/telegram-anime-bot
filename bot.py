import telebot
from telebot.types import Message
from config import BOT_TOKEN
from downloader import aria2_add

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN não definido nas variáveis de ambiente")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(msg: Message):
    bot.reply_to(
        msg,
        "🤖 <b>Anime Downloader Bot</b>\n\n"
        "Envie o comando:\n"
        "<code>/baixar LINK</code>\n\n"
        "Suporte:\n"
        "• Magnet\n"
        "• Links diretos\n"
        "• nyaa.si"
    )

@bot.message_handler(commands=["baixar"])
def baixar(msg: Message):
    try:
        parts = msg.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(msg, "❌ Envie o link junto com o comando.\nEx: /baixar LINK")
            return

        link = parts[1].strip()

        r = aria2_add(link)

        if "result" in r:
            bot.reply_to(msg, "⬇️ <b>Download iniciado com sucesso!</b>")
        else:
            bot.reply_to(msg, f"❌ Erro ao iniciar download:\n<code>{r}</code>")

    except Exception as e:
        bot.reply_to(msg, f"❌ Erro interno:\n<code>{e}</code>")

print("🤖 Bot iniciado com sucesso!")
bot.infinity_polling()
