from PIL import Image, ImageDraw
import imageio
import os
import qrcode

def create_qr_code_with_links(links, qr_size=128):
    qr_images = []
    
    for link in links:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((qr_size, qr_size))
        qr_images.append(qr_img)
    
    return qr_images

def create_animated_gif_from_images(folder_path, output_gif, output_size, download_links):
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png','.webp','.svg','.bmp','.gif'))]

    images = []
    qr_code_images = create_qr_code_with_links(download_links)
    
    for image_file in image_files:
        image = Image.open(os.path.join(folder_path, image_file))
        resized_image = resize_image(image, output_size)
        images.append(resized_image)
    
    images += qr_code_images

    imageio.mimsave(output_gif, images, duration=0.5)

    print(f"Animated GIF with input images from folder '{folder_path}' created as '{output_gif}'")

# Function to resize image
def resize_image(image, output_size):
    return image.resize(output_size)

# Path to the input folder containing image files
input_folder_path = "input"

# Path to the output folder for the animated GIF
output_folder_path = "output"
os.makedirs(output_folder_path, exist_ok=True)

# Specify download links for the QR codes
download_links = ["https://example.com/download1", "https://example.com/download2"]

# Specify the output animated GIF file
output_gif = os.path.join(output_folder_path, "animated_images.gif")

# Output image size for resizing
output_size = (256, 256)  # Adjust the size as needed

create_animated_gif_from_images(input_folder_path, output_gif, output_size, download_links)