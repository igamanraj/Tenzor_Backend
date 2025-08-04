from dotenv import load_dotenv
import os
load_dotenv()


SERVER_URL = "localhost"
PORT = int(os.getenv("PORT", 8900))  # Use env variable or default to 8900
ENV = "dev"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")