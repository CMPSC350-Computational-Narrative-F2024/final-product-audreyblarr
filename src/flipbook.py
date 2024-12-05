import os
import openai
from dotenv import dotenv_values
import requests
from PIL import Image
from io import BytesIO
import img2pdf
from fpdf import FPDF


# Load environment variables
CONFIG = dotenv_values(".env")
OPEN_AI_KEY = CONFIG.get("KEY") or os.environ.get("OPEN_AI_KEY")
OPEN_AI_ORG = CONFIG.get("ORG") or os.environ.get("OPEN_AI_ORG")

# Set OpenAI API credentials
openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

def generate_og_image(prompt):
    response = openai.images.generate(
        prompt=prompt,
        model="dall-e-2",
        size="1024x1024"
    )
    image_url = response.data[0].url
    image_response = requests.get(image_url)
    img = Image.open(BytesIO(image_response.content))
    return img

def convert_to_pdf(image, name):
    with BytesIO() as output:
        image.save(output, format="PNG")
        image_bytes = output.getvalue()
    with open(f"{name}.pdf", "wb") as f:
        f.write(img2pdf.convert(image_bytes))

def save_image_as_png(image, name):
    image = image.convert("RGBA")
    image.save(f"{name}.png", format="PNG")

def generate_image_edit(name, prompt):
    with open(f"{name}.png", "rb") as image_file:
        response = openai.images.edit(
            image=image_file,
            mask=open("transparent.png", "rb"),
            prompt=prompt,
            size="1024x1024"
        )
    image_url = response.data[0].url
    image_response = requests.get(image_url)
    img = Image.open(BytesIO(image_response.content))
    return img

#prompt1 = "Generate a hyper-realistic image of an orange cat. The cat must be standing in a field of flowers, capturing the side profile of the cat with its full body in frame."
#og_image = generate_og_image(prompt1)
#save_image_as_png(og_image, "image1")
#convert_to_pdf(og_image, "image1")

prompt2 = "Edit the image to portray the same exact cat, taking a running step forward from its previous standing position. The cat should be in motion, with one paw lifted off the ground. The rest of the image, including the background, should remain exactly the same."
image_2 = generate_image_edit("image1", prompt2)
save_image_as_png(image_2, "image2")
convert_to_pdf(image_2, "image2")

prompt3 = "Edit the image to portray the same exact cat, jumping from the previous standing position. The cat should appear in motion, with both front paws in the air. The rest of the image, including the background, should remain exactly the same."
image_3 = generate_image_edit("image1", prompt3)
save_image_as_png(image_3, "image3")
convert_to_pdf(image_3, "image3")