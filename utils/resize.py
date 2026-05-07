import os
from PIL import Image

def get_min_size(image_folder):
    min_width, min_height = float('inf'), float('inf')
    
    for filename in os.listdir(image_folder):
        filepath = os.path.join(image_folder, filename)
        if os.path.isfile(filepath):
            with Image.open(filepath) as img:
                width, height = img.size
                min_width = min(min_width, width)
                min_height = min(min_height, height)
    
    return min_width, min_height

def resize_images(image_folder, target_size):
    for filename in os.listdir(image_folder):
        filepath = os.path.join(image_folder, filename)
        if os.path.isfile(filepath):
            with Image.open(filepath) as img:
                resized_img = img.resize(target_size, Image.LANCZOS)  # High-quality interpolation
                resized_img.save(filepath)

# Set your folders
real_folder = r'C:\Users\HUAWEI\Desktop\Graduation project\Face-detection\data\image-real'
fake_folder = r'C:\Users\HUAWEI\Desktop\Graduation project\Face-detection\data\image-fake'

# Get minimum size from both folders
min_real_size = get_min_size(real_folder)
min_fake_size = get_min_size(fake_folder)

# Get the smallest size across both folders
min_size = (min(min_real_size[0], min_fake_size[0]), min(min_real_size[1], min_fake_size[1]))

# Print the smallest size found
print(f"The smallest image size is: {min_size}")

# Resize all images in both folders to the smallest size
resize_images(real_folder, min_size)
resize_images(fake_folder, min_size)

print("All images have been resized to the smallest size.")
