import streamlit as st
import google.generativeai as genai

# वेबसाइट की सेटिंग
st.set_page_config(page_title="Jeet AI TTS", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# आपकी API Key (इसे सुरक्षित रखें)
genai.configure(api_key="AIzaSyBcIaGxdPLHr75LCHdcK-UjrSqAjUu14pg")

text = st.text_area("यहाँ अपना टेक्स्ट लिखें:", placeholder="नमस्ते, मैं आपकी कैसे मदद कर सकता हूँ?")

if st.button("Generate"):
    if text:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Convert to speech instructions: {text}")
        st.success("AI ने आपका टेक्स्ट प्रोसेस कर लिया है!")
        st.write(response.text)
    else:
        st.warning("कृपया कुछ लिखें।")
