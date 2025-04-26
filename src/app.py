import streamlit as st
import os
from pathlib import Path
from src.bot import UniAssistantBot

# Set page config
st.set_page_config(
    page_title="Uni Assistant Bot",
    page_icon="🎓",
    layout="wide"
)

# Initialize the bot
@st.cache_resource
def get_bot():
    return UniAssistantBot()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Common questions in Thai and English
THAI_QUESTIONS = {
    "การสมัครเรียน": {
        "ช่องทางการสมัคร": "ช่องทางการสมัครเรียนมีอะไรบ้าง?",
        "ความแตกต่างของเทอม": "เทอม 1/1 และ 1/2 แตกต่างกันอย่างไร?",
        "เอกสารที่จำเป็น": "ต้องใช้เอกสารอะไรบ้างในการสมัคร?"
    },
    "การลงทะเบียน": {
        "การสมัครออนไลน์": "ขั้นตอนการลงทะเบียนออนไลน์เป็นอย่างไร?",
        "เอกสารรายงานตัว": "ต้องเตรียมเอกสารอะไรบ้างในการรายงานตัว?"
    },
    "หลักสูตร": {
        "หลักสูตรนานาชาติ": "หลักสูตรนานาชาติมีอะไรบ้าง?"
    },
    "สิ่งอำนวยความสะดวก": {
        "พื้นที่ทำงานร่วมกัน": "มีพื้นที่ทำงานร่วมกันที่ไหนบ้าง?",
        "สถานที่ออกกำลังกาย": "มีสถานที่ออกกำลังกายอะไรบ้าง?"
    },
    "การเดินทาง": {
        "การเดินทางด้วยรถสาธารณะ": "เดินทางมาที่มหาวิทยาลัยได้อย่างไร?"
    }
}

ENGLISH_QUESTIONS = {
    "Admission": {
        "Admission channels": "What are the admission channels?",
        "Term differences": "What are the differences between Term 1/1 and 1/2?",
        "Required documents": "What documents are required for admission?"
    },
    "Registration": {
        "Online registration": "What is the online registration process?",
        "Reporting documents": "What documents do I need for reporting?"
    },
    "Programs": {
        "International programs": "What international programs are available?"
    },
    "Facilities": {
        "Coworking spaces": "Where are the coworking spaces?",
        "Sports facilities": "What sports facilities are available?"
    },
    "Transportation": {
        "Public transportation": "How can I get to the university?"
    }
}

# Sidebar with information and buttons
with st.sidebar:
    st.title("Uni Assistant Bot")
    
    # Thai Section
    st.markdown("""
    ### บอทช่วยเหลือนักศึกษา
    
    บอทช่วยเหลือที่ให้ข้อมูลเกี่ยวกับมหาวิทยาลัย
    
    คุณสามารถสอบถามเกี่ยวกับ:
    """)
    
    # Thai question buttons
    for category, questions in THAI_QUESTIONS.items():
        st.markdown(f"**{category}**")
        for subcategory, question in questions.items():
            if st.button(question, key=f"th_{category}_{subcategory}"):
                st.session_state.messages.append({"role": "user", "content": question})
                bot = get_bot()
                response = bot.handle_message(question)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
    
    st.markdown("---")  # Add a separator
    
    # English Section
    st.markdown("""
    ### Uni Assistant Bot
    
    A helpful assistant for university-related information.
    
    You can ask questions about:
    """)
    
    # English question buttons
    for category, questions in ENGLISH_QUESTIONS.items():
        st.markdown(f"**{category}**")
        for subcategory, question in questions.items():
            if st.button(question, key=f"en_{category}_{subcategory}"):
                st.session_state.messages.append({"role": "user", "content": question})
                bot = get_bot()
                response = bot.handle_message(question)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

# Main chat interface
st.title("Uni Assistant Bot")
st.markdown("ถามอะไรเกี่ยวกับมหาวิทยาลัยก็ได้! (Ask me anything about the university!)")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("ต้องการทราบข้อมูลเกี่ยวกับอะไร? / What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    bot = get_bot()
    response = bot.handle_message(prompt)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)

# Add a clear chat button
if st.button("ล้างประวัติการสนทนา (Clear Chat)"):
    st.session_state.messages = []
    st.rerun() 