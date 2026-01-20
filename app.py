import streamlit as st
import google.generativeai as genai
from gtts import gTTS

# पेज सेटिंग
st.set_page_config(page_title="Jeet AI Voice", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# अपनी नई API Key यहाँ डालें (AIzaSy...)
genai.configure(api_key="AIzaSyB-Sza7a8-S0siJAYxCN-5Tt94bUf-h7eI")

text_input = st.text_area("यहाँ लिखें:", placeholder="नमस्ते जीत!")

if st.button("Generate Voice"):
    if text_input:
        try:
            # हमने यहाँ सबसे स्टेबल मॉडल 'gemini-pro' या 'gemini-1.5-flash' का चुनाव किया है
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # सुरक्षित तरीके से कंटेंट जनरेट करना
            response = model.generate_content(text_input)
            
            if response.text:
                st.success("AI जवाब तैयार है!")
                st.write(response.text)

                # आवाज़ (Audio) फ़ाइल बनाना
                tts = gTTS(text=response.text, lang='hi') 
                tts.save("voice.mp3")
                
                # ऑडियो प्लेयर लोड करना
                with open("voice.mp3", "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
            
        except Exception as e:
            st.error(f"Error details: {e}")
            st.info("सुझाव: Google AI Studio में जाकर पक्का करें कि आपकी API Key Active है।")
    else:
        st.warning("कृपया कुछ टाइप करें।")
