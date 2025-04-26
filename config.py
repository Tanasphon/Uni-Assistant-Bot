import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/unibot_db')

# Bot Settings
BOT_NAME = "Uni Assistant Bot"
BOT_VERSION = "1.0.0"
MAX_CONTEXT_LENGTH = 4000
MAX_RESPONSE_TOKENS = 500

# University Information
UNIVERSITY_NAME = "Your University Name"
DEPARTMENTS = {
    "CS": "Computer Science",
    "EE": "Electrical Engineering",
    "ME": "Mechanical Engineering",
    # Add more departments as needed
}

# FAQ Categories
FAQ_CATEGORIES = [
    "registration",
    "schedule",
    "academic",
    "financial",
    "activities",
    "general"
] 