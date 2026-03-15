from google import genai
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    #contents="Explain how AI works in a few words"
    contents="Explain how AI works in simple words"
)

print(response.text)