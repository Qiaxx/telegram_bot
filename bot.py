from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')


app = ApplicationBuilder().token("6917585855:AAGbKQ2bH3EtCJ8tPl-mUlvw6JCisRs_vxU").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()
