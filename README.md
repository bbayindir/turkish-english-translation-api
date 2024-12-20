# Turkish-English Translation API with TDK Integration

This project is a simple API that fetches a word (**Bir Kelime**) from the Turkish Language Association (TDK), translates it into English using Google Translator, and returns both the Turkish word and its English translation.

   ![image](https://github.com/user-attachments/assets/cdca39b5-21e7-4c9c-abc6-732e209c5907)

## Features:
- Fetches a word from TDK API under the "Bri Kelime" heading.
- Translates the word from Turkish to English.
- Provides Swagger UI for API documentation.

## Requirements:
To get this project up and running on your local machine, you will need:

- Python 3.6+
- `pip` (Python package manager)

## Installation:

Follow the steps below to set up the Project on Windows CMD:

1. **Clone the repository:**

   Open your terminal or command prompt and run the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/bbayindir/turkish-english-translation-api.git
   ```
2. **Navigate to the project directory:**
   Change your directory to the project folder:
   ```bash
   cd turkish-english-translation-api
   ```
3. **Create and activate a virtual environment (optional but recommended):**
   It's good practice to use a virtual environment to manage project dependencies:
   ```bash
   python -m venv venv
   ```
   ```bash
   venv\Scripts\activate
   ```
4. **Install dependencies:**
   Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   If you don't have a requirements.txt file, you can manually install the necessary packages:
    ```bash
   pip install flask flask-restx requests deep-translator
   ```
5. **Run the application:**
   Once the dependencies are installed, you can run the application using the following command:
   ```bash
   python app.py
   ```
6. **Access the Swagger UI:**
   Once the application is running, you can access the Swagger UI to test the API and view the documentation at:
   ```bash
   http://localhost:5000
   ```
7. **Testing the API:**
  To test the /translate endpoint, you can use Swagger UI, or simply make a GET request to:
   ```bash
   http://localhost:5000/translate
   ```

