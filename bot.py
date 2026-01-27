import os
import telebot
from telebot.types import Message

# ==============================
# CONFIGURAÇÃO
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN não definido nas variáveis de ambiente")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# ==============================
# COMANDOS
# ==============================

@bot.message_handler(commands=["start"])
def start(msg: Message):
    bot.reply_to(
        msg,
        "🤖 <b>Anime Downloader Bot</b>\n\n"
        "Como usar:\n"
        "<code>/baixar LINK</code>\n\n"
        "⚠️ (Modo teste)\n"
        "No momento o bot apenas valida o link.\n"
        "O download real será ativado no próximo passo."
    )

@bot.message_handler(commands=["baixar"])
def baixar(msg: Message):
    parts = msg.text.split(maxsplit=1)

    if len(parts) < 2:
        bot.reply_to(
            msg,
            "❌ Você precisa enviar o link junto com o comando.\n\n"
            "Exemplo:\n<code>/baixar https://nyaa.si/view/XXXX</code>"
        )
        return

    link = parts[1].strip()

    # TESTE — apenas confirma que recebeu o link
    bot.reply_to(
        msg,
        "✅ <b>Link recebido com sucesso!</b>\n\n"
        f"<code>{link}</code>\n\n"
        "🚧 Download será ativado em breve."
    )

# ==============================
# INICIALIZAÇÃO
# ==============================

print("🤖 Bot iniciado com sucesso!")
bot.infinity_polling(skip_pending=True)
