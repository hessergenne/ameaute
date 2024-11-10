import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")
        return None
