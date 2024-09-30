from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

# Define your bot token
TOKEN = "6894015834:AAHY8TBmvZOTGK2djKasnCyAlUBYPwKlAtM"

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello welcome to the WoHooRK bot, How may I be of service?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to start\nUse /email for my email\nUse /linkedin for my LinkedIn profile\nUse /github for my GitHub")

async def outlook_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("rohankaushik2001@outlook.com")

async def linkedin_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://www.linkedin.com/in/rohan-kaushik10")

async def github_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://github.com/ROH4NK4U5H1K")

# For unknown commands
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sorry, '{update.message.text}' is not a valid command.")

# For unknown text messages
async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sorry, I can't recognize what you said: '{update.message.text}'.")

# Main function to run the bot
async def main():
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('email', outlook_url))
    application.add_handler(CommandHandler('linkedin', linkedin_url))
    application.add_handler(CommandHandler('github', github_url))

    # Add message handlers for unknown commands and text
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), unknown_text))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Initialize and start the bot
    await application.initialize()
    await application.start()

    # Wait until the application is stopped
    await application.wait_for_stop()

if __name__ == '__main__':
    # Set the event loop policy to avoid RuntimeError on Windows
    if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())  # This is Windows-specific

    asyncio.run(main())
