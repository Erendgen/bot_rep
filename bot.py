from telegram.ext import Updater, CommandHandler
import settings

def start_bott(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start_bott))
    mybot.start_polling()
    mybot.idle()
main()