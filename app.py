import streamlit as st
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="Jeet AI Voice", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# यहाँ अपनी नई API Key डालें
genai.configure(api_key="AIzaSyB9OycJSZjGUJ-CCXq6t-JJuksncFQzMJ0")

text_input = st.text_area("यहाँ लिखें:", placeholder="नमस्ते जीत!")

if st.button("Generate Voice"):
    if text_input:
        try:
            # यह मॉडल 404 एरर को फिक्स करने के लिए सबसे अच्छा है
            model = genai.GenerativeModel('gemini-pro')
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
