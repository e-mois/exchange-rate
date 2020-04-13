from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(update, context):
    text = 'Вызван /start'
    update.message.reply_text(text)
    logging.info('Called /start')

def talk_to_me(update, context):
    user_text = 'Привет {}'.format(update.message.chat.first_name)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
            update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_TELEGRAM_KEY, use_context=True)

    logging.info('Bot started')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling() #ходи в телеграм
    mybot.idle() #работай пока не остановлю


main()