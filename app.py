import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# वेबसाइट की सेटिंग
st.set_page_config(page_title="Jeet AI Voice", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# API Key सेटअप
genai.configure(api_key="AIzaSyBcIaGxdPLHr75LCHdcK-UjrSqAjUu14pg")

text_input = st.text_area("यहाँ अपना मैसेज लिखें:", placeholder="नमस्ते, मैं जीत हूँ!")

if st.button("Generate Voice"):
    if text_input:
        try:
            # हम सीधे मॉडल को कॉल कर रहे हैं
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(text_input)
            
            clean_text = response.text
            st.success("AI ने जवाब तैयार कर लिया है!")
            st.write(clean_text)

            # आवाज़ (Audio) बनाना - gTTS का उपयोग करके
            tts = gTTS(text=clean_text, lang='hi') 
            tts.save("speech.mp3")
            
            # ऑडियो प्लेयर दिखाना
            with open("speech.mp3", "rb") as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")
            
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("सुझाव: अगर 404 एरर आता है, तो एक बार नया API Key बनाकर देखें।")
    else:
        st.warning("कृपया कुछ टाइप करें।")
