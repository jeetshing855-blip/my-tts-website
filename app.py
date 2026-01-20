import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

st.set_page_config(page_title="Jeet AI Voice", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# Secrets से API Key उठाना
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("कृपया Streamlit Secrets में API Key जोड़ें।")

text_input = st.text_area("यहाँ लिखें:", placeholder="नमस्ते जीत!")

if st.button("Generate Voice"):
    if text_input:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(text_input)
            
            if response.text:
                st.success("AI जवाब तैयार है!")
                st.write(response.text)

                tts = gTTS(text=response.text, lang='hi') 
                tts.save("voice.mp3")
                
                with open("voice.mp3", "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("कृपया कुछ टाइप करें।")
