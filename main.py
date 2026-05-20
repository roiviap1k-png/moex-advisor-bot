from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = "СЮДА_ПОТОМ_ВСТАВИМ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "MOEX Advisor запущен.\n\n"
        "Команды:\n"
        "/рынок\n"
        "/анализ SBER"
    )

async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Рынок РФ\n\n"
        "Модуль аналитики подключим дальше."
    )

async def analyse(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Пример:\n/анализ SBER"
        )
        return

    ticker = context.args[0].upper()

    text = (
        f"{ticker}\n\n"
        "Тренд: анализируется\n"
        "Риск: анализируется\n\n"
        "Материал носит информационно-аналитический "
        "характер и не является "
        "индивидуальной инвестиционной рекомендацией."
    )

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("рынок", market)
)

app.add_handler(
    CommandHandler("анализ", analyse)
)

app.run_polling()
