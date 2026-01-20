import streamlit as st
import google.generativeai as genai

# वेबसाइट की सेटिंग
st.set_page_config(page_title="Jeet AI TTS", page_icon="🎙️")
st.title("🎙️ Jeet's AI Voice Generator")

# आपकी API Key
genai.configure(api_key="AIzaSyBcIaGxdPLHr75LCHdcK-UjrSqAjUu14pg")

text = st.text_area("यहाँ अपना टेक्स्ट लिखें:", placeholder="नमस्ते!")

if st.button("Generate"):
    if text:
        try:
            # हम सबसे लेटेस्ट और स्टेबल मॉडल का नाम इस्तेमाल कर रहे हैं
            model = genai.GenerativeModel('gemini-1.5-flash') 
            response = model.generate_content(text)
            st.success("सफलता!")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("कृपया कुछ टाइप करें।")
