import telebot
from telebot.types import Message
from config import BOT_TOKEN
from seedr_api import add_torrent

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN não configurado")

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
        "• Torrent\n"
        "• nyaa.si\n\n"
        "⚠️ Modo atual: API externa (Seedr)"
    )


@bot.message_handler(commands=["baixar"])
def baixar(msg: Message):
    parts = msg.text.split(maxsplit=1)

    if len(parts) < 2:
        bot.reply_to(
            msg,
            "❌ Envie o link junto com o comando.\n"
            "Exemplo:\n<code>/baixar magnet:?xt=...</code>"
        )
        return

    link = parts[1].strip()

    bot.reply_to(msg, "🔎 Link recebido, enviando para o Seedr...")

    try:
        r = add_torrent(link)

        if "user_torrent_id" in r:
            bot.reply_to(
                msg,
                "✅ <b>Download iniciado com sucesso!</b>\n\n"
                "⏳ O Seedr está processando o arquivo.\n"
                "🔔 Você será notificado quando estiver pronto."
            )
        else:
            bot.reply_to(msg, f"⚠️ Resposta inesperada:\n<code>{r}</code>")

    except Exception as e:
        bot.reply_to(
            msg,
            "❌ Erro ao enviar para o Seedr:\n"
            f"<code>{e}</code>"
        )


print("🤖 Bot iniciado com sucesso!")
bot.infinity_polling()
# ==== KEEP ALIVE (Railway) ====
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online 🚀"

def run_web():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_web, daemon=True).start()
