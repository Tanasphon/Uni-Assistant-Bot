import logging
import google.generativeai as genai
import os
from pathlib import Path
import re
from dotenv import load_dotenv

# Import local modules
from .university_info import UniversityInfo

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Load environment variables
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    logger.warning("GEMINI_API_KEY not found in environment variables. Some features may not work properly.")

# Initialize Google Generative AI
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    logger.error(f"Failed to initialize Gemini API: {e}")
    model = None

class UniAssistantBot:
    def __init__(self):
        self.university_info = UniversityInfo()
        self.setup_genai()
        self.thai_chars = r'[\u0E00-\u0E7F]'
        
    def setup_genai(self):
        """Initialize the Gemini model."""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            logging.warning("GEMINI_API_KEY not found in environment variables")
            self.model = None
            return
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        except Exception as e:
            logging.error(f"Error initializing Gemini model: {e}")
            self.model = None

    def _is_thai_text(self, text: str) -> bool:
        """Check if the text contains Thai characters."""
        return bool(re.search(self.thai_chars, text))
        
    def get_greeting(self, user_message: str) -> str:
        """Return appropriate greeting based on language."""
        is_thai = self._is_thai_text(user_message)
        if is_thai:
            return "สวัสดีค่ะ มีอะไรให้ช่วยไหมคะ?"
        return "Hello! How can I help you today?"

    def get_help_message(self, user_message: str) -> str:
        """Return help message in appropriate language."""
        is_thai = self._is_thai_text(user_message)
        if is_thai:
            return """ฉันสามารถช่วยคุณเกี่ยวกับ:
1. ข้อมูลการรับสมัคร
2. ความแตกต่างระหว่างเทอม
3. เอกสารที่จำเป็น
4. การเดินทาง
5. การลงทะเบียนออนไลน์
6. การรายงานตัว
7. โปรแกรมนานาชาติ
8. พื้นที่ทำงานร่วมกัน
9. สิ่งอำนวยความสะดวกด้านกีฬา

คุณสามารถถามคำถามได้เลยค่ะ"""
        return """I can help you with:
1. Admission information
2. Term differences
3. Required documents
4. Transportation
5. Online registration
6. Document reporting
7. International programs
8. Coworking spaces
9. Sports facilities

Feel free to ask any questions!"""

    def handle_message(self, user_message: str) -> str:
        """Process user message and return appropriate response."""
        is_thai = self._is_thai_text(user_message)
        
        # Check for basic commands
        lower_message = user_message.lower()
        if any(word in lower_message for word in ['hello', 'hi', 'สวัสดี']):
            return self.get_greeting(user_message)
        if any(word in lower_message for word in ['help', 'ช่วย', 'ทำอะไรได้']):
            return self.get_help_message(user_message)

        # Check for specific topics
        if any(word in lower_message for word in ['admission', 'สมัคร', 'รับสมัคร']):
            return self.university_info.get_admission_channels(user_message)
        if any(word in lower_message for word in ['term', 'เทอม']):
            return self.university_info.get_term_differences(user_message)
        if any(word in lower_message for word in ['document', 'เอกสาร']):
            return self.university_info.get_required_documents(user_message)
        if any(word in lower_message for word in ['transport', 'เดินทาง']):
            return self.university_info.get_transportation(user_message)
        if any(word in lower_message for word in ['register', 'ลงทะเบียน']):
            return self.university_info.get_online_registration(user_message)
        if any(word in lower_message for word in ['report', 'รายงานตัว']):
            return self.university_info.get_reporting_documents(user_message)
        if any(word in lower_message for word in ['international', 'นานาชาติ']):
            return self.university_info.get_international_program(user_message)
        if any(word in lower_message for word in ['coworking', 'ทำงาน']):
            return self.university_info.get_coworking_spaces(user_message)
        if any(word in lower_message for word in ['sport', 'กีฬา']):
            return self.university_info.get_sports_facilities(user_message)

        # Use Gemini for general responses
        if not self.model:
            return "ขออภัยค่ะ ไม่สามารถเชื่อมต่อกับระบบได้ในขณะนี้" if is_thai else "Sorry, I cannot connect to the system at the moment."
        
        try:
            prompt = f"You are a university assistant bot. Please respond in {'Thai' if is_thai else 'English'} to: {user_message}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "ขออภัยค่ะ ไม่สามารถประมวลผลคำถามได้" if is_thai else "Sorry, I cannot process your question at the moment."

def main():
    """Start the bot."""
    bot = UniAssistantBot()
    print(bot.get_greeting(""))
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
            
        response = bot.handle_message(user_input)
        print(f"\nBot: {response}")

if __name__ == '__main__':
    main() 