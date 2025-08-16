import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("EURON_API_KEY")

API_URL = "https://api.euron.one/api/v1/euri/images/generations"

def generate_image(prompt, size="1024x1024", style="vivid", n=1):
    payload = {
        "prompt": prompt,
        "model": "black-forest-labs/FLUX.1-schnell",
        "n": n,
        "size": size,
        "quality": "standard",
        "response_format": "url",
        "style": style
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["data"][0]["url"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
