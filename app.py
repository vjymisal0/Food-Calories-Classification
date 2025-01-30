from dotenv import load_dotenv

load_dotenv()  ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Initialize our streamlit app

st.set_page_config(page_title="Gemini Health App", page_icon="🍎", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .description {
        font-size:16px;
        color: #666;
    }
    .stButton>button {
        background-color: #31326f;
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
    }
    
    </style>
    """, unsafe_allow_html=True)

# App Title and Description
st.markdown('<p class="big-font">🍎 Gemini Health App</p>', unsafe_allow_html=True)
st.markdown('<p class="description">Upload an image of your meal, and we\'ll calculate the total calories for you!</p>', unsafe_allow_html=True)

# Sidebar for additional information
with st.sidebar:
    st.markdown("### About")
    st.markdown("This app uses Google's Gemini Pro Vision API to analyze food images and estimate the total calories. Simply upload an image of your meal, and the app will provide a detailed breakdown of the calories in each food item.")

# Main content
col1, col2 = st.columns([3, 2])

with col1:
    input = st.text_input("Input Prompt: ", key="input", placeholder="Enter any specific instructions or details about the meal...")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

with col2:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
"""

## If submit button is clicked

if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_repsonse(input_prompt, image_data, input)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please upload an image before submitting.")