import requests
from stegano import lsb

def decrypt(text, s):
    result = ""
    for char in text:
        # Handle only visible ASCII characters (from 32 to 126)
        if 32 <= ord(char) <= 126:
            result += chr((ord(char) - s - 32) % 95 + 32)
        else:
            result += char  # Leave non-ASCII characters as they are
    return result

def download_image_from_url(image_url, save_path):
    # Download the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved as {save_path}")
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")

def reveal_message_from_image(image_path):
    # Extract the hidden message from the image
    return lsb.reveal(image_path)

# Set the Caesar cipher shift value used in encryption
s = int(input("What's your shift value?: "))

# Encrypted image URL to decrypt (includes special characters)
encrypted_url = input("Paste your encrypted link here: ")
decrypted_url = decrypt(encrypted_url, s)

# Download the image from the decrypted URL
downloaded_image_path = "downloaded_image.png"
download_image_from_url(decrypted_url, downloaded_image_path)

# Reveal the hidden message (encrypted password) from the downloaded image
encrypted_password_in_image = reveal_message_from_image(downloaded_image_path)

# Decrypt the hidden password
decrypted_password = decrypt(encrypted_password_in_image, s)

print(f"Decrypted Image URL: {decrypted_url}")
print(f"Decrypted Password: {decrypted_password}")
