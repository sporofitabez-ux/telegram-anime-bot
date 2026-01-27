import telebot
from telebot.types import Message
from config import BOT_TOKEN
from downloader import aria2_add

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(msg: Message):
    bot.reply_to(
        msg,
        "🤖 <b>Anime Downloader Bot</b>\n\n"
        "📥 Como usar:\n"
        "<code>/baixar LINK</code>\n\n"
        "📌 Suporte:\n"
        "• Magnet\n"
        "• Links diretos\n"
        "• nyaa.si\n\n"
        "⚠️ Modo atual: <b>API externa</b>"
    )


@bot.message_handler(commands=["baixar"])
def baixar(msg: Message):
    parts = msg.text.split(maxsplit=1)

    if len(parts) < 2:
        bot.reply_to(
            msg,
            "❌ Envie o link junto com o comando.\n"
            "Exemplo:\n<code>/baixar magnet:...</code>"
        )
        return

    link = parts[1].strip()

    bot.reply_to(msg, "🔍 Link recebido, processando...")

    result = aria2_add(link)

    if "result" in result:
        bot.send_message(
            msg.chat.id,
            "✅ <b>Link enviado com sucesso!</b>\n"
            "⏳ Download será processado externamente.\n\n"
            "🔔 Você será notificado quando estiver pronto."
        )
    else:
        bot.send_message(
            msg.chat.id,
            f"❌ Erro ao enviar link:\n<code>{result}</code>"
        )


print("🤖 Bot iniciado com sucesso")
bot.infinity_polling()
