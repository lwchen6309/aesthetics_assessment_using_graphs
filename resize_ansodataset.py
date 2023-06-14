import os
from PIL import Image

def upscale_images(directory, target_size):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Modify extensions as per your requirement
            filepath = os.path.join(directory, filename)
            image = Image.open(filepath)
            width, height = image.size
            smallest_dimension = min(width, height)
            if smallest_dimension < target_size:
                scale_factor = target_size / smallest_dimension
                new_width = int(width * scale_factor)
                new_height = int(height * scale_factor)
                resized_image = image.resize((new_width, new_height))
                resized_image.save(filepath)  # Overwrite the original image with the upscaled version
                resized_image.close()
                print(f"Upscaled image: {filename} (Original size: {width}x{height}, Upscaled size: {new_width}x{new_height})")
            else:
                image.close()

# Directory containing the images
directory = 'datasetImages_originalSize'

# Target size for upscaling
target_size = 220

# Upscale the images if their smallest dimension is less than target_size
upscale_images(directory, target_size)