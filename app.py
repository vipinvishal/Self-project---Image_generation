import streamlit as st
from backend import generate_image

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🖼️ AI Image Generator")

prompt = st.text_area("Enter your prompt:", "A beautiful sunset over mountains")
size = st.selectbox("Choose image size", ["512x512", "1024x1024", "2048x2048"])
style = st.selectbox("Choose style", ["vivid", "natural", "fantasy"])

if st.button("Generate Image"):
    try:
        image_url = generate_image(prompt, size, style)
        st.image(image_url, caption="Generated Image", use_container_width=True)
        st.markdown(f"[🔗 Download Image]({image_url})")
    except Exception as e:
        st.error(str(e))

