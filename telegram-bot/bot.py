from telegram.ext import Application, CommandHandler
import asyncio

async def start(update, context):
    await update.message.reply_text("Добро пожаловать в MedBook!")

def main():
    application = Application.builder().token("TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()