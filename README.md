# Turkish-English Translation API with TDK Integration

This project is a simple API that fetches a word from the Turkish Language Association (TDK), translates it into English using Google Translator, and returns both the Turkish word and its English translation.

## Features:
- Fetches a word from TDK API under the "Bir Kelime" heading.
- Translates the word from Turkish to English.
- Provides Swagger UI for API documentation.

## Requirements:
To get this project up and running on your local machine, you will need:

- Python 3.6+
- `pip` (Python package manager)

## Installation:

Follow these steps to set up the project:

1. **Clone the repository:**

   Open your terminal or command prompt and run the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/turkish-english-translation-api.git

2. **Navigate to the project directory:**

Change your directory to the project folder:

```bash
Copy code
cd turkish-english-translation-api
Create and activate a virtual environment (optional but recommended):

3. **It's good practice to use a virtual environment to manage project dependencies:**

```bash
Copy code
python -m venv venv
On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file, you can manually install the necessary packages:

bash
Copy code
pip install flask flask-restx requests deep-translator
Run the application:

Once the dependencies are installed, you can run the application using the following command:

bash
Copy code
python app.py
Access the Swagger UI:

Once the application is running, you can access the Swagger UI to test the API and view the documentation at:

bash
Copy code
http://localhost:5000/swagger/
Testing the API:

To test the /translate endpoint, you can use Swagger UI, or simply make a GET request to:

bash
Copy code
http://localhost:5000/translate
The response will contain a random Turkish word fetched from TDK along with its English translation.
