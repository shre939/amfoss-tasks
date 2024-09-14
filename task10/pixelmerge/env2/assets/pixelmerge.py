import os
import cv2
import numpy as np
from PIL import Image, ImageDraw

assets_folder = '/home/shreya/Documents/pixelmerge/env2/assets'

# renamed each file  layerx.png as x.png
image_files = sorted([f for f in os.listdir(assets_folder) if f.endswith('.png')], key=lambda x: int(x.split('.')[0]))

# Initialize variables to store the previous centroid and color for drawing
previous_centroid = None
previous_color = None

# Create a new blank image to draw on (size depends on your needs, adjust as necessary)
output_image = Image.new("RGB", (2000, 2000), (255, 255, 255))
draw = ImageDraw.Draw(output_image)

# Loop through each image file
for image_file in image_files:
    image_path = os.path.join(assets_folder, image_file)
    print(f"Processing image: {image_path}")
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error loading image: {image_path}")
        continue

    # Check if the image is completely white
    if np.all(image == 255):
        # Line break: reset the previous centroid and color
        previous_centroid = None
        previous_color = None
        continue

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define lower and upper thresholds for white
    lower_white = np.array([200, 200, 200], dtype=np.uint8)
    upper_white = np.array([255, 255, 255], dtype=np.uint8)

    # Create a binary mask where white pixels are filtered out
    mask = cv2.inRange(image, lower_white, upper_white)

    # Invert the mask to keep the colored regions
    mask = cv2.bitwise_not(mask)

    # Find contours of the dot
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Assume the largest contour is the dot
        contour = max(contours, key=cv2.contourArea)

        # Calculate moments for the contour
        M = cv2.moments(contour)

        # Compute the centroid coordinates of the dot
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        else:
            continue  # No valid centroid found, skip to the next image

        # Get BGR values of the dot at the centroid coordinates
        bgr_values = image[cy, cx]

        # Convert BGR to RGB for PIL drawing
        dot_color = (int(bgr_values[2]), int(bgr_values[1]), int(bgr_values[0]))  # Convert BGR to RGB

        # Draw a line from the previous centroid to the current one if there is a previous centroid
        if previous_centroid is not None:
            draw.line([previous_centroid, (cx, cy)], fill=previous_color, width=2)

        # Update the previous centroid and color
        previous_centroid = (cx, cy)
        previous_color = dot_color

# Save the output image
output_image.save('output_image.png')
print("Output image saved as 'output_image.png'")