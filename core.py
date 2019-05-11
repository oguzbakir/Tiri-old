import logging
from random import choice
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = open("secrets.cfg", "r").readline().strip()
#print(TOKEN)
def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="How can i help you?")

def mock(update, context):
	sentence = update.message.reply_to_message.text
	logging.info("mock")
	mockedText = ''.join(choice((str.upper, str.lower))(c) for c in sentence)
	context.bot.send_message(chat_id=update.message.chat_id, text=mockedText)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
mock_handler = CommandHandler('mock', mock)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(mock_handler)

updater.start_polling()

