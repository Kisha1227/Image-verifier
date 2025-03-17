import requests
from PIL import Image
from io import BytesIO
import google.generativeai as genai

# Initialize the Gemini API client
genai.configure(api_key="AIzaSyA_cVwS9XqomAfh0jFJ2Kk1MBByGCOvPwY")

# Download and open the image
url = "https://cdn.shopify.com/s/files/1/0086/0795/7054/files/Golden-Retriever.jpg?v=1645179525"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

# Generate content (description of the image)
response = model.generate_content([image, "Tell me about this image"])

# Print the result
print(response.text)
