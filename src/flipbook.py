import os
import openai # type: ignore
from dotenv import dotenv_values # type: ignore
import requests # type: ignore
from PIL import Image # type: ignore
from io import BytesIO
import img2pdf # type: ignore
import PyPDF2 # type: ignore


CONFIG = dotenv_values(".env")
OPEN_AI_KEY = CONFIG.get("KEY") or os.environ.get("OPEN_AI_KEY")
OPEN_AI_ORG = CONFIG.get("ORG") or os.environ.get("OPEN_AI_ORG")

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

def merge_pdfs(pdf_list, output_name):
    pdf_merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        pdf_merger.append(pdf)
    with open(output_name, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

prompt1 = "Generate a hyper-realistic image of an orange cat. The cat must be standing in a field of flowers, capturing the side profile of the cat with its full body in frame."
og_image = generate_og_image(prompt1)
save_image_as_png(og_image, "image1")
convert_to_pdf(og_image, "image1")

prompt2 = "Edit the image to portray the same cat. The cat should have its body low to the ground, preparing to pounce."
image_2 = generate_image_edit("image1", prompt2)
save_image_as_png(image_2, "image2")
convert_to_pdf(image_2, "image2")

prompt3 = "Edit the image to portray the same cat. The cat should be in a crouched position with its back end high in the air, ready to pounce. Its tail should be in the air."
image_3 = generate_image_edit("image1", prompt3)
save_image_as_png(image_3, "image3")
convert_to_pdf(image_3, "image3")

prompt4 = "Edit the image to portray the same cat. The cat should have its right front paw slightly lifted off the ground, ready to leap into the air. The rest of its paws should remain planted on the ground."
image_4 = generate_image_edit("image1", prompt4)
save_image_as_png(image_4, "image4")
convert_to_pdf(image_4, "image4")

prompt5 = "Edit the image to portray the same cat. The cat should be in mid-leap, with its front paws extended forward and its back paws pushing off the ground. The cat's body should be elongated, showing the motion of leaping forward."
image_5 = generate_image_edit("image1", prompt5)
save_image_as_png(image_5, "image5")
convert_to_pdf(image_5, "image5")

prompt6 = "Edit the image to portray the same cat. The cat should begin to push off the ground with its hind legs, just starting to leap forward, with both front paws off the ground. "
image_6 = generate_image_edit("image1", prompt6)
save_image_as_png(image_6, "image6")
convert_to_pdf(image_6, "image6")

prompt7 = "Edit the image to portray the same cat. The cat should be completely mid-air, with all its legs off the ground and extended."
image_7 = generate_image_edit("image1", prompt7)
save_image_as_png(image_7, "image7")
convert_to_pdf(image_7, "image7")

prompt8 = "Edit the image to portray the same cat. The cat should be landing its leap on its front paws, with its back paws still off the ground."
image_8 = generate_image_edit("image1", prompt8)
save_image_as_png(image_8, "image8")
convert_to_pdf(image_8, "image8")

prompt9 = "Edit the image to portray the same cat. The cat should be landing its back legs on the ground, with its front right paw slightly off the ground and its front left paw still planted, ready to leap again. "
image_9 = generate_image_edit("image1", prompt9)
save_image_as_png(image_9, "image9")
convert_to_pdf(image_9, "image9")

prompt10 = "Edit the image to portray the same cat. The cat should have its front paws up and off the ground, with all its weight on its hind legs."
image_10 = generate_image_edit("image1", prompt10)
save_image_as_png(image_10, "image10")
convert_to_pdf(image_10, "image10")

prompt11 = "Edit the image to return to the standing cat from the original."
image_11 = generate_image_edit("image1", prompt11)
save_image_as_png(image_11, "image11")
convert_to_pdf(image_11, "image11")

prompt12 = "Edit the image to portray the same cat. The cat should have its body low to the ground, preparing to pounce."
image_12 = generate_image_edit("image1", prompt12)
save_image_as_png(image_12, "image12")
convert_to_pdf(image_12, "image12")

prompt13 = "Edit the image to portray the same cat. The cat should be in a crouched position with its back end high in the air, ready to pounce. Its tail should be in the air."
image_13 = generate_image_edit("image1", prompt13)
save_image_as_png(image_13, "image13")
convert_to_pdf(image_13, "image13")

prompt14 = "Edit the image to portray the same cat. The cat should have its right front paw slightly lifted off the ground, ready to leap into the air. The rest of its paws should remain planted on the ground."
image_14 = generate_image_edit("image1", prompt14)
save_image_as_png(image_14, "image14")
convert_to_pdf(image_14, "image14")

prompt15 = "Edit the image to portray the same cat. The cat should be in mid-leap, with its front paws extended forward and its back paws pushing off the ground. The cat's body should be elongated, showing the motion of leaping forward."
image_15 = generate_image_edit("image1", prompt15)
save_image_as_png(image_15, "image15")
convert_to_pdf(image_15, "image15")

prompt16 = "Edit the image to portray the same cat. The cat should begin to push off the ground with its hind legs, just starting to leap forward, with both front paws off the ground. "
image_16 = generate_image_edit("image1", prompt16)
save_image_as_png(image_16, "image16")
convert_to_pdf(image_16, "image16")

prompt17 = "Edit the image to portray the same cat. The cat should be completely mid-air, with all its legs off the ground and extended."
image_17 = generate_image_edit("image1", prompt17)
save_image_as_png(image_17, "image17")
convert_to_pdf(image_17, "image17")

prompt18 = "Edit the image to portray the same cat. The cat should be landing its leap on its front paws, with its back paws still off the ground."
image_18 = generate_image_edit("image1", prompt18)
save_image_as_png(image_18, "image18")
convert_to_pdf(image_18, "image18")

prompt19 = "Edit the image to portray the same cat. The cat should be landing its back legs on the ground, with its front right paw slightly off the ground and its front left paw still planted, ready to leap again. "
image_19 = generate_image_edit("image1", prompt19)
save_image_as_png(image_19, "image19")
convert_to_pdf(image_19, "image19")

prompt20 = "Edit the image to portray the same cat. The cat should have its front paws up and off the ground, with all its weight on its hind legs."
image_20 = generate_image_edit("image1", prompt20)
save_image_as_png(image_20, "image20")
convert_to_pdf(image_20, "image20")

prompt21 = "Edit the image to portray the same cat. The cat should have its body low to the ground, preparing to pounce."
image_21 = generate_image_edit("image1", prompt21)
save_image_as_png(image_21, "image21")
convert_to_pdf(image_21, "image21")

prompt22 = "Edit the image to portray the same cat. The cat should be in a crouched position with its back end high in the air, ready to pounce. Its tail should be in the air."
image_22 = generate_image_edit("image1", prompt22)
save_image_as_png(image_22, "image22")
convert_to_pdf(image_22, "image22")

prompt23 = "Edit the image to portray the same cat. The cat should have its right front paw slightly lifted off the ground, ready to leap into the air. The rest of its paws should remain planted on the ground."
image_23 = generate_image_edit("image1", prompt23)
save_image_as_png(image_23, "image23")
convert_to_pdf(image_23, "image23")

prompt24 = "Edit the image to portray the same cat. The cat should be in mid-leap, with its front paws extended forward and its back paws pushing off the ground. The cat's body should be elongated, showing the motion of leaping forward."
image_24 = generate_image_edit("image1", prompt24)
save_image_as_png(image_24, "image24")
convert_to_pdf(image_24, "image24")

prompt25 = "Edit the image to portray the same cat. The cat should begin to push off the ground with its hind legs, just starting to leap forward, with both front paws off the ground. "
image_25 = generate_image_edit("image1", prompt25)
save_image_as_png(image_25, "image25")
convert_to_pdf(image_25, "image25")

pdf_files = [
    "image1.pdf",
    "image2.pdf",
    "image3.pdf",
    "image4.pdf",
    "image5.pdf",
    "image6.pdf",
    "image7.pdf",
    "image8.pdf",
    "image9.pdf",
    "image10.pdf",
    "image11.pdf",
    "image12.pdf",
    "image13.pdf",
    "image14.pdf",
    "image15.pdf",
    "image16.pdf",
    "image17.pdf",
    "image18.pdf",
    "image19.pdf",
    "image20.pdf",
    "image21.pdf",
    "image22.pdf",
    "image23.pdf",
    "image24.pdf",
    "image25.pdf"
]

merge_pdfs(pdf_files, "combined_images.pdf")