# University FAQ Chatbot 🎓
# แชทบอทตอบคำถามเกี่ยวกับมหาวิทยาลัย

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.29.0-FF4B4B.svg)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-orange)](https://ai.google.dev/)

[English](#english) | [ภาษาไทย](#thai)

---

<a name="english"></a>
## 🌟 Overview

An intelligent chatbot designed to provide information about university-related queries. The bot supports both Thai and English languages, automatically detecting the user's preferred language and responding accordingly.

### 🚀 Features

- **Bilingual Support**: Automatically detects and responds in Thai or English
- **Pre-defined Topics**:
  - Admission channels and information
  - Term differences
  - Required documents
  - Transportation options
  - Online registration procedures
  - Document reporting
  - International programs
  - Coworking spaces
  - Sports facilities
- **AI-Powered**: Uses Google's Gemini AI for handling general queries
- **Modern UI**: Built with Streamlit for a clean and responsive interface

### 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/university-faq-chatbot.git
cd university-faq-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Create a `.env` file in the root directory
- Add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 🎯 Usage

Run the application:
```bash
python run.py
```

The web interface will be available at `http://localhost:8501`

### 📁 Project Structure

```
university-faq-chatbot/
├── src/
│   ├── app.py           # Streamlit UI
│   ├── bot.py           # Chatbot core logic
│   ├── university_info.py # University information handler
│   └── __init__.py
├── data/
│   └── university_info.json # FAQ data
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
├── run.py              # Entry point
└── README.md           # Documentation
```

---

<a name="thai"></a>
## 🌟 ภาพรวม

แชทบอทอัจฉริยะที่ออกแบบมาเพื่อให้ข้อมูลเกี่ยวกับคำถามต่างๆ ของมหาวิทยาลัย รองรับทั้งภาษาไทยและภาษาอังกฤษ โดยระบบจะตรวจจับภาษาที่ผู้ใช้ต้องการโดยอัตโนมัติ

### �� คุณสมบัติ

- **รองรับ 2 ภาษา**: ตรวจจับและตอบกลับอัตโนมัติทั้งภาษาไทยและอังกฤษ
- **หัวข้อที่รองรับ**:
  - ช่องทางและข้อมูลการรับสมัคร
  - ความแตกต่างระหว่างเทอม
  - เอกสารที่จำเป็น
  - ตัวเลือกการเดินทาง
  - ขั้นตอนการลงทะเบียนออนไลน์
  - การรายงานตัวและเอกสาร
  - โปรแกรมนานาชาติ
  - พื้นที่ทำงานร่วม
  - สิ่งอำนวยความสะดวกด้านกีฬา
- **ขับเคลื่อนด้วย AI**: ใช้ Google Gemini AI สำหรับคำถามทั่วไป
- **UI ทันสมัย**: สร้างด้วย Streamlit สำหรับอินเตอร์เฟซที่สะอาดและตอบสนองได้ดี

### 🛠️ การติดตั้ง

1. โคลนโปรเจค:
```bash
git clone https://github.com/yourusername/university-faq-chatbot.git
cd university-faq-chatbot
```

2. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

3. ตั้งค่าตัวแปรสภาพแวดล้อม:
- สร้างไฟล์ `.env` ในไดเรกทอรีหลัก
- เพิ่ม Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 🎯 การใช้งาน

รันแอปพลิเคชัน:
```bash
python run.py
```

เว็บอินเตอร์เฟซจะพร้อมใช้งานที่ `http://localhost:8501`

### 📁 โครงสร้างโปรเจค

```
university-faq-chatbot/
├── src/
│   ├── app.py           # Streamlit UI
│   ├── bot.py           # โค้ดหลักของแชทบอท
│   ├── university_info.py # ตัวจัดการข้อมูลมหาวิทยาลัย
│   └── __init__.py
├── data/
│   └── university_info.json # ข้อมูล FAQ
├── .env                 # ตัวแปรสภาพแวดล้อม
├── requirements.txt     # Dependencies
├── run.py              # จุดเริ่มต้นโปรแกรม
└── README.md           # เอกสาร
```

## Features

- 🤖 Multi-platform support (Telegram and LINE)
- 📚 Course information lookup
- 📝 Student records search
- ❓ FAQ system
- 🎓 Department-specific information
- 📊 Data management from CSV files
- 🤝 Natural language processing for better interaction

## Prerequisites

- Python 3.8 or higher
- Telegram Bot Token
- LINE Messaging API credentials
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Tanasphon/Uni-Assistant-Bot.git
cd Uni-Assistant-Bot
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
```

## Usage

1. Add your CSV files to the `data` directory
2. Start the bot:
```bash
python main.py
```

3. For Telegram:
   - Search for your bot using the bot's username
   - Start a chat with the bot
   - Use the `/start` command to begin

4. For LINE:
   - Add the bot as a friend using the LINE QR code
   - Start chatting with the bot

## Available Commands

- `/start` - Start the bot and get welcome message
- `/help` - Show available commands
- `/datasets` - List available datasets
- `/info [dataset]` - Get information about a specific dataset

## Data Format

Place your CSV files in the `data` directory. The bot will automatically load all CSV files and make them available for querying.

Example CSV structure (courses.csv):
```csv
course_code,course_name,department,credits,prerequisites,description
CS101,Introduction to Programming,Computer Science,3,None,Basic programming concepts
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