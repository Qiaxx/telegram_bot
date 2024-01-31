import textwrap

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackContext
import utils


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}\n\n'
                                    f'Я могу выводить курсы валют или конкретной валюты, а так же '
                                    f'конвертировать определеную валюту в выбранную по текущему курсу')


async def convert_to_ruble(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Введите название валюты (например: USD или EUR): ')

    async def handle_text_message(updat: Update, context: CallbackContext) -> None:
        user_answer = updat.message.text.upper()
        text_ = utils.main(user_answer)
        await update.message.reply_text(text_)

    app.add_handler(MessageHandler(None, handle_text_message))


app = ApplicationBuilder().token("6917585855:AAGbKQ2bH3EtCJ8tPl-mUlvw6JCisRs_vxU").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("rub", convert_to_ruble))
app.run_polling()
