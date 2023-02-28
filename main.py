import requests
from PIL import Image
url = "https://api.nasa.gov/planetary/apod"
api_key = "YOUR_API_KEY"
def save_apod_image(date, file_path):
    # Construct the API request URL
    params = {"date": date, "api_key": api_key}
    response = requests.get(url, params=params)

    # Get the image URL from the API response
    data = response.json()
    image_url = data["url"]

    # Download the image and save it to file
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    else:
        print("Failed to download image: %s" % response.status_code)
