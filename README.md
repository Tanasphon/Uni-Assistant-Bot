# Uni Assistant Bot

A comprehensive university assistant chatbot that helps students with academic information, schedules, and general university-related queries.

## Features

- 🤖 Multi-platform support (Telegram and LINE)
- 📚 Course schedule management
- 📝 Registration assistance
- ❓ FAQ system
- 🎓 Department-specific information
- 📊 Student data management
- 🤝 Natural language processing for better interaction

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- Telegram Bot Token
- LINE Messaging API credentials
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/uni-assistant-bot.git
cd uni-assistant-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```
TELEGRAM_TOKEN=your_telegram_bot_token
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
LINE_CHANNEL_SECRET=your_line_channel_secret
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/unibot_db
```

5. Set up the PostgreSQL database:
```bash
psql -U your_username -d unibot_db -f database.sql
```

## Usage

1. Start the bot:
```bash
python bot.py
```

2. For Telegram:
   - Search for your bot using the bot's username
   - Start a chat with the bot
   - Use the `/start` command to begin

3. For LINE:
   - Add the bot as a friend using the LINE QR code
   - Start chatting with the bot

## Available Commands

- `/start` - Start the bot and get welcome message
- `/help` - Show available commands
- `/schedule` - Get your class schedule
- `/registration` - Get registration information
- `/faq` - Browse frequently asked questions

## Project Structure

```
uni-assistant-bot/
├── bot.py              # Main bot application
├── config.py           # Configuration settings
├── database.py         # Database operations
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Development Team: Jeehan.sutt@bumail.net 