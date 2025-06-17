import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = st.secrets["OPENAI_API_KEY"]


# Configure the Gemini API
genai.configure(api_key=api_key)

# Use a correct model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="🎉 Event Idea Generator", layout="centered")
st.title("🎉 Event Idea Generator")
st.write("Enter a topic, and get 10 creative event ideas with short and simple descriptions!")

# Input prompt
topic = st.text_input("Enter a topic (e.g. health, education, tech for students):")

if st.button("Generate Ideas"):
    if not topic:
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("Generating ideas..."):
            prompt = (
                f"Generate 10 creative event ideas for the topic: {topic}. "
                "Each idea should have a short, clear title and a 2-3 line easy-to-understand description. "
                "Use simple language for general public."
            )
            try:
                response = model.generate_content(prompt)
                st.success("✅ Ideas generated successfully!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Error generating ideas:\n\n{str(e)}")
