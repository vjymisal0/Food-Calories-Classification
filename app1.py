from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import base64

app = Flask(__name__)
load_dotenv()  # Load environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image_data):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image_data])
    return response.text

def process_image(image_file):
    image_bytes = image_file.read()
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')
    image_data = {
        "mime_type": image_file.content_type,
        "data": encoded_image
    }
    return image_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    image_file = request.files['image']
    input_text = request.form.get("input", "")
    image_data = process_image(image_file)

    prompt = """
    You are a nutrition expert. Analyze the food items in the image and calculate the total calories.
    Provide details of each food item in this format:
    1. Item 1 - No. of calories
    2. Item 2 - No. of calories
    """

    response_text = get_gemini_response(prompt, image_data)
    return jsonify({"calorie_info": response_text})

if __name__ == '__main__':
    app.run(debug=True)
