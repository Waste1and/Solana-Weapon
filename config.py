# config.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
API_URL = os.getenv("API_URL")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
