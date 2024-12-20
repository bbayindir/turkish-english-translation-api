from flask import Flask, jsonify
from flask_restx import Api, Resource
import requests
from deep_translator import GoogleTranslator

# Create Flask application
app = Flask(__name__)

# Initialize Flask-RESTX API with Swagger documentation
api = Api(app, version='1.0', title='Turkish-English Translation API',
          description='Translates words from TDK (Turkish Language Association) and shows their English equivalents.')

# Function to get a word from TDK API
def fetch_tdk_word():
    url = "https://sozluk.gov.tr/icerik"
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Connection": "keep-alive"
        }
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract the first "madde" value from the "kelime" field in the JSON response
        word_list = data.get("kelime", [])
        if word_list:
            word = word_list[0].get("madde", None)
            return word
        else:
            return None
    except Exception as e:
        print(f"Error fetching data from TDK API: {e}")
        return None

# Function to translate a word using Deep Translator
def translate_word(word):
    # Translate the word from Turkish to English
    translation = GoogleTranslator(source='tr', target='en').translate(word)
    return translation

# Define the /translate endpoint with Swagger documentation
@api.route('/translate')
class Translate(Resource):
    def get(self):
        """Fetches a word from TDK, translates it into English, and returns both the Turkish and English versions.
        
        The Turkish word is fetched from TDK's "Bir Kelime" section.
        This word is the one listed under the "Bir Kelime" heading of TDK's dictionary.
        """
        # Fetch a word from TDK API
        tdk_word = fetch_tdk_word()
        if tdk_word:
            # Translate the word into English
            english_translation = translate_word(tdk_word)
        else:
            tdk_word = "Could not fetch word from TDK"
            english_translation = "Translation not available"

        # Return the result in JSON format
        return jsonify({
            "turkish": tdk_word,
            "english": english_translation
        })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
