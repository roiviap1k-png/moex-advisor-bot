from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

import os

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "MOEX Advisor\n\n"
        "Команды:\n"
        "/рынок\n"
        "/анализ SBER"
    )

    await update.message.reply_text(text)


async def market(update: Update, context):

    await update.message.reply_text(
        "Российский рынок анализируется."
    )


async def analyse(update: Update, context):

    if not context.args:

        await update.message.reply_text(
            "Пример:\n/анализ SBER"
        )
        return

    ticker = context.args[0].upper()

    text = (
        f"{ticker}\n\n"
        "Статус: модуль аналитики скоро подключим.\n\n"
        "Материал носит информационно-аналитический "
        "характер и не является индивидуальной "
        "инвестиционной рекомендацией."
    )

    await update.message.reply_text(text)


app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CommandHandler(
        "рынок",
        market
    )
)

app.add_handler(
    CommandHandler(
        "анализ",
        analyse
    )
)

app.run_polling()
