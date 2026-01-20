import streamlit as st
import google.generativeai as genai

# वेबसाइट की सेटिंग
st.set_page_config(page_title="Jeet AI TTS", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# आपकी API Key
genai.configure(api_key="AIzaSyBcIaGxdPLHr75LCHdcK-UjrSqAjUu14pg")

text = st.text_area("यहाँ अपना टेक्स्ट लिखें:", placeholder="नमस्ते, मैं आपकी कैसे मदद कर सकता हूँ?")

if st.button("Generate"):
    if text:
        try:
            # यहाँ हमने मॉडल का नाम बदला है जो फ्री में चलता है
           model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(f"You are a TTS assistant. Process this text: {text}")
            
            st.success("AI ने आपका टेक्स्ट प्रोसेस कर लिया है!")
            st.write(response.text)
        except Exception as e:
            st.error(f"अभी भी एरर आ रहा है: {e}")
    else:
        st.warning("कृपया पहले कुछ लिखें।")
