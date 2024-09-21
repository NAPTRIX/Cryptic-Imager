# Cryptic-Imager
Cryptic Imager is a Python tool that securely hides encrypted text inside images using steganography and uploads them to imgbb. It encrypts sensitive information like passwords with a Caesar cipher before embedding it in an image.

## Features

- Encrypts sensitive text using a Caesar cipher.
- Hides the encrypted text in an image using steganography.
- Uploads the image to a free image hosting service (imgbb).
- Decrypts the URL and the hidden text for easy retrieval.

## Required Libraries

To run this project, you will need the following Python libraries:

- `stegano`: For steganography functions.
- `requests`: For making HTTP requests to the imgbb API.

You can install the required libraries using pip:

```bash
pip install stegano requests
```
## imgbb API Key

An imgbb API key is required for the image upload process. You can obtain a free API key by signing up on [imgbb](https://imgbb.com/).

## Usage

### Encryption Script

Set the following parameters at the beginning of the script:

- **text**: The sensitive information (e.g., password) to encrypt.
- **shift**: The shift value for the Caesar cipher.
- **image_path**: Path to the original image.
- **output_image**: Path to save the output image with the hidden message.
- **api_key**: Your imgbb API key for uploading images.

Run the encryption script to hide the encrypted text in the image and upload it to imgbb.

### Decryption Script

1. Set the Caesar cipher shift value (`s`) and the encrypted image URL.
2. Run the decryption script to download the image, reveal the hidden message, and decrypt it.
