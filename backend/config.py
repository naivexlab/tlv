import os
from dotenv import load_dotenv

load_dotenv()

# Get API Key from environment variable
WHOIS_API_KEY = os.getenv("WHOIS_API_KEY")