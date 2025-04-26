import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
import openai
from config import *
import psycopg2
from psycopg2.extras import RealDictCursor

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Initialize Line Bot
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

class UniAssistantBot:
    def __init__(self):
        self.db_connection = self._init_db()
        
    def _init_db(self):
        try:
            return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            return None

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /start is issued."""
        welcome_message = (
            f"👋 Welcome to {BOT_NAME}!\n\n"
            "I'm here to help you with university-related questions. "
            "You can ask me about:\n"
            "• Course schedules\n"
            "• Registration information\n"
            "• Academic requirements\n"
            "• University activities\n"
            "• And more!\n\n"
            "Type /help to see available commands."
        )
        await update.message.reply_text(welcome_message)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /help is issued."""
        help_text = (
            "Available commands:\n"
            "/start - Start the bot\n"
            "/help - Show this help message\n"
            "/schedule - Get your class schedule\n"
            "/registration - Get registration information\n"
            "/faq - Browse frequently asked questions\n"
            "\nYou can also ask me any questions about university life!"
        )
        await update.message.reply_text(help_text)

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages."""
        user_message = update.message.text
        try:
            # Process the message using OpenAI
            response = await self._process_message(user_message)
            await update.message.reply_text(response)
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await update.message.reply_text("I'm sorry, I encountered an error. Please try again later.")

    async def _process_message(self, message: str) -> str:
        """Process user message using OpenAI."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are {BOT_NAME}, a helpful university assistant. "
                     "Provide accurate and concise information about university-related topics."},
                    {"role": "user", "content": message}
                ],
                max_tokens=MAX_RESPONSE_TOKENS
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return "I'm sorry, I'm having trouble processing your request right now."

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", UniAssistantBot().start))
    application.add_handler(CommandHandler("help", UniAssistantBot().help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, UniAssistantBot().handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main() 