import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# वेबसाइट की सेटिंग
st.set_page_config(page_title="Jeet AI Voice", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# API Key सेटअप
genai.configure(api_key="AIzaSyBcIaGxdPLHr75LCHdcK-UjrSqAjUu14pg")

text_input = st.text_area("यहाँ अपना मैसेज लिखें:", placeholder="नमस्ते, आप कैसे हैं?")

if st.button("Generate Voice"):
    if text_input:
        try:
            # लेटेस्ट मॉडल का इस्तेमाल
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(text_input)
            
            clean_text = response.text
            st.success("AI ने टेक्स्ट प्रोसेस कर लिया है!")
            st.write(clean_text)

            # आवाज़ (Audio) बनाना
            tts = gTTS(text=clean_text, lang='hi') # हिंदी भाषा के लिए
            tts.save("speech.mp3")
            
            # ऑडियो प्लेयर दिखाना
            audio_file = open("speech.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("कृपया कुछ टाइप करें।")
