import json
from pathlib import Path
import re
import logging
from typing import Dict, Any, Optional

class UniversityInfo:
    def __init__(self):
        self.data_dir = Path(__file__).parent.parent / "data"
        self.data_file = self.data_dir / "university_info.json"
        self.data = self._load_data()
        self.thai_chars = r'[\u0E00-\u0E7F]'
        
    def _load_data(self) -> Dict[str, Any]:
        """Load data from JSON file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                logging.info("Successfully loaded data from JSON file")
                return data
        except FileNotFoundError:
            logging.error(f"Data file not found at {self.data_file}")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return {}
        except Exception as e:
            logging.error(f"Unexpected error loading data: {e}")
            return {}
            
    def _is_thai_text(self, text: str) -> bool:
        """
        Check if the text contains Thai characters.
        Returns True if ANY Thai character is found in the text.
        """
        if not text:
            return False
        return bool(re.search(self.thai_chars, text))
        
    def _get_response(self, path: str, is_thai: bool) -> str:
        """
        Get response in the appropriate language.
        Falls back gracefully if the requested language or path is not available.
        """
        try:
            parts = path.split('.')
            current = self.data
            
            # Navigate through the nested structure
            for part in parts:
                if part not in current:
                    raise KeyError(f"Path segment '{part}' not found in data")
                current = current[part]
            
            # Try to get response in requested language
            if is_thai and 'th' in current:
                return current['th']
            elif not is_thai and 'en' in current:
                return current['en']
            
            # Fallback: if requested language not available, try the other language
            if is_thai and 'en' in current:
                logging.warning(f"Thai response not found for {path}, falling back to English")
                return f"(English response only) {current['en']}"
            elif not is_thai and 'th' in current:
                logging.warning(f"English response not found for {path}, falling back to Thai")
                return f"(Thai response only) {current['th']}"
            
            # If no response available in either language
            raise KeyError("No response available in any language")
            
        except Exception as e:
            logging.error(f"Error getting response for path {path}: {e}")
            if is_thai:
                return "ขออภัย ไม่พบข้อมูลที่ต้องการในขณะนี้ กรุณาลองใหม่อีกครั้งในภายหลัง"
            return "Sorry, the requested information is not available at the moment. Please try again later."
    
    def get_admission_channels(self, user_message: str) -> str:
        """Get admission channels information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("admission.channels", is_thai)
    
    def get_term_differences(self, user_message: str) -> str:
        """Get term differences information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("admission.terms", is_thai)
    
    def get_required_documents(self, user_message: str) -> str:
        """Get required documents information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("admission.documents", is_thai)
    
    def get_transportation(self, user_message: str) -> str:
        """Get transportation information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("transportation", is_thai)
    
    def get_online_registration(self, user_message: str) -> str:
        """Get online registration information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("registration.online", is_thai)
    
    def get_reporting_documents(self, user_message: str) -> str:
        """Get reporting documents information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("registration.reporting", is_thai)
    
    def get_international_program(self, user_message: str) -> str:
        """Get international program information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("international", is_thai)
    
    def get_coworking_spaces(self, user_message: str) -> str:
        """Get coworking spaces information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("facilities.coworking", is_thai)
    
    def get_sports_facilities(self, user_message: str) -> str:
        """Get sports facilities information in the appropriate language."""
        is_thai = self._is_thai_text(user_message)
        return self._get_response("facilities.sports", is_thai) 