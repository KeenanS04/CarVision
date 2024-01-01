from PIL import Image, ImageOps
import numpy as np

def preprocess_image(image_path):
    desired_size = 224

    with Image.open(image_path) as img:
        # Calculate the padding
        old_size = img.size
        ratio = float(desired_size) / max(old_size)
        new_size = tuple([int(x * ratio) for x in old_size])

        # Resize the image to fit within 224x224, maintaining aspect ratio
        img = img.resize(new_size, Image.Resampling.LANCZOS)  # Updated resampling method

        # Create a new image with white background and paste the resized image
        new_img = Image.new("RGB", (desired_size, desired_size), (255, 255, 255))
        new_img.paste(img, ((desired_size - new_size[0]) // 2, 
                           (desired_size - new_size[1]) // 2))

        # Convert to numpy array and normalize
        img_array = np.asarray(new_img)
        img_array = img_array / 255.0  # Normalize to [0, 1]

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        return img_array
