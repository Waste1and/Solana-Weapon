from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Solana private key
API_URL = os.getenv("API_URL")  # Solana API URL
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # Discord bot token
