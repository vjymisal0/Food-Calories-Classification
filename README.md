<div align="center">
  
# Gemini Health App

</div>
<div align="center">
  
![Gemini Health App Demo](gif/health.gif)
  
</div>
A Streamlit app that uses Google's Gemini Pro Vision API to analyze food images and estimate total calories.

## Table of Contents
-----------------

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Usage](#usage)
6. [License](#license)

## Overview
------------

The Gemini Health App is designed to help users estimate the total calories in their meals by analyzing food images. The app utilizes Google's Gemini Pro Vision API to identify food items and calculate their respective calorie counts.

## Features
------------

*   Image analysis using Google's Gemini Pro Vision API
*   Estimation of total calories in a meal
*   Detailed breakdown of calories in each food item
*   User-friendly interface built with Streamlit

## Requirements
------------

*   Python 3.7+
*   Streamlit
*   Google Cloud API key with Gemini Pro Vision API enabled
*   dotenv

## Setup
--------

1.  Clone the repository: `git clone https://github.com/vjymisal0/Food-Calories-Classification.git`
2.  Install required dependencies: `pip install -r requirements.txt`
3.  Create a `.env` file with your Google Cloud API key: `GOOGLE_API_KEY=your-api-key`
4.  Load environment variables: `load_dotenv()`
5.  Run the app: `streamlit run app.py`

## Usage
-----

1.  Upload a food image
2.  Enter any specific instructions or details about the meal (optional)
3.  Click the "Tell me the total calories" button
4.  View the estimated total calories and detailed breakdown of calories in each food item

## License
-------

This project is licensed under the MIT License. See LICENSE for details.

## Contributing
------------

Contributions are welcome! Please submit a pull request with your changes.

## Acknowledgments
--------------

*   Google Cloud for providing the Gemini Pro Vision API
*   Streamlit for providing a user-friendly interface framework
