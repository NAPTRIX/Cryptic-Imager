
from stegano import lsb
import requests
import base64

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def hide_message_in_image(image_path, secret_message, output_image):
    # Encode the secret message in the image using steganography
    secret_image = lsb.hide(image_path, secret_message)
    secret_image.save(output_image)

def upload_image_to_imgbb(image_path, api_key):
    # Open the image file and read it as binary
    with open(image_path, "rb") as image_file:
        # Convert the image to Base64 string
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    
    # send the image in Base64 format to the imgbb API
    response = requests.post(
        "https://api.imgbb.com/1/upload",
        data={
            "key": api_key,
            "image": image_base64,  # Base64-encoded image string
        },
    )

    # Print the full response for debugging
    response_data = response.json()
    print("Full response:", response_data)  # Debugging information (can be commented out)

    if "data" in response_data:
        return response_data["data"]["url"]
    else:
        raise Exception(f"Error uploading image: {response_data}")

# Encrypt password
text = "mypassword"
shift = 4
encrypted_password = encrypt(text, shift)

# Use steganography to hide the encrypted password in an image
hide_message_in_image("original_image.png", encrypted_password, "output_image.png")

# Upload the image to imgbb
api_key = "your_api_key"  # Your imgbb API key (https://api.imgbb.com/)
uploaded_image_url = upload_image_to_imgbb("output_image.png", api_key)

# Encrypt the link to the uploaded image
encrypted_url = encrypt(uploaded_image_url, shift)

print(f"Encrypted Password: {encrypted_password}")
print(f"Encrypted Image URL: {encrypted_url}")
