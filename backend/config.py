import os
from dotenv import load_dotenv

load_dotenv()

# Get API Key from environment variable, fallback to hardcoded key
WHOIS_API_KEY = os.getenv("WHOIS_API_KEY", "PASTE_YOUR_KEY_HERE")