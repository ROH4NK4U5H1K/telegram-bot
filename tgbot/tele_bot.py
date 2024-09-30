from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("6894015834:AAHY8TBmvZOTGK2djKasnCyAlUBYPwKlAtM", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello welcome to the WoHooRK bot, How may I bee of service? ")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to start\n. use ")

def outlook_url(update: Update, context: CallbackContext):
    update.message.reply_text("rohankaushik2001@outlook.com")

def linkedin_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/rohan-kaushik10")

def github_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://github.com/ROH4NK4U5H1K")

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('email', outlook_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
