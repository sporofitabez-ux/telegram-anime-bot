from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN
from downloader import download_link

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot de downloads de anime\n\n"
        "Use:\n"
        "/baixar <link>\n\n"
        "Suporta magnet, nyaa.si e links diretos."
    )

async def baixar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Envie o link junto com o comando.")
        return

    link = context.args[0]
    await update.message.reply_text("⬇️ Download iniciado...")

    try:
        download_link(link)
        await update.message.reply_text("✅ Download adicionado com sucesso!")
    except Exception as e:
        await update.message.reply_text(f"❌ Erro: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("baixar", baixar))

    print("🤖 Bot rodando...")
    app.run_polling()
