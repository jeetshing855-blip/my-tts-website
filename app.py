import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# वेबसाइट की सेटिंग
st.set_page_config(page_title="Jeet AI Voice", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# यहाँ अपनी नई सुरक्षित API Key डालें
genai.configure(api_key="AIzaSyB9OycJSZjGUJ-CCXq6t-JJuksncFQzMJ0")

text_input = st.text_area("यहाँ अपना मैसेज लिखें:", placeholder="नमस्ते, मैं जीत हूँ!")

if st.button("Generate Voice"):
    if text_input:
        try:
            # स्टेबल मॉडल का उपयोग
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(text_input)
            
            clean_text = response.text
            st.success("AI ने जवाब तैयार कर लिया है!")
            st.write(clean_text)

            # आवाज़ (Audio) बनाना
            tts = gTTS(text=clean_text, lang='hi') 
            tts.save("speech.mp3")
            
            # ऑडियो प्लेयर दिखाना
            with open("speech.mp3", "rb") as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("कृपया कुछ टाइप करें।")
