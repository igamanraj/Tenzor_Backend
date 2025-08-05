from dotenv import load_dotenv
import os
load_dotenv()


SERVER_URL = "0.0.0.0"  # Changed for deployment
PORT = int(os.getenv("PORT", 8900))  # Use env variable or default to 8900
ENV = os.getenv("ENV", "dev")  # Get from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")