from PIL import Image
import os

# Define standard dimensions for all images
TARGET_WIDTH = 1200
TARGET_HEIGHT = 675  # 16:9 aspect ratio

# Directory containing images
image_dir = '/home/ubuntu/smartnests/images'

# List of images to standardize
images_to_standardize = [
    'workspace_laptop_tablet.jpeg',
    'financial_monitors.jpeg',
    'business_meeting.jpeg',
    'customer_service.jpeg'
]

for image_name in images_to_standardize:
    image_path = os.path.join(image_dir, image_name)
    
    # Open the image
    img = Image.open(image_path)
    
    # Resize the image while maintaining aspect ratio
    img = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)
    
    # Save the resized image, overwriting the original
    img.save(image_path)
    
    print(f"Resized {image_name} to {TARGET_WIDTH}x{TARGET_HEIGHT}")

print("All images have been standardized to the same dimensions.")
