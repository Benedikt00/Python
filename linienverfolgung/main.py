import cv2
from PIL import Image, ImageDraw
import numpy as np
import random
import matplotlib.pyplot as plt


# Initialize the webcam
cap = cv2.VideoCapture(1)  # 0 indicates the default webcam (you can change it if necessary)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Read a single frame from the webcam
ret, frame = cap.read()

# Check if the frame was read successfully
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Specify the path where you want to save the image
image_path = "captured_image.jpg"

# Save the frame as an image
cv2.imwrite(image_path, frame)

cap.release()

print(f"Image saved as {image_path}")

# Close any open OpenCV windows (if any)
cv2.destroyAllWindows()

# Open the saved image using Pillow
image = Image.open(image_path)

# Convert the image to an RGB array
rgb_array = np.array(image)

# Check the shape of the RGB array (height, width, channels)
mid = round(len(rgb_array)/2)

stripe = rgb_array[mid].tolist()

samples = 100
length = len(stripe)
locations = [random.randint(0, length-1) for _ in range(samples)]
rgb_loc = []
for x in locations:
    rgb_loc.append(stripe[x])

rgb_median = []
for i in range(len(rgb_loc[0])):
    so = sorted(rgb_loc, key=lambda x: x[i])
    rgb_median.append(so[round(len(so)/2)][i])

for x, pixel in enumerate(stripe):
    abweichung = 0
    for i, rgb in enumerate(pixel):
        abweichung += abs(rgb_median[i] - pixel[i])


    stripe[x].append(x)
    stripe[x].append(abweichung)


stso = sorted(stripe, key=lambda x: x[-1], reverse=True)


x_coords = []
y_coords = []

for x in stso:
    x_coords.append(x[-2])
    y_coords.append(x[-1])

# Create a scatter plot of the points
plt.scatter(x_coords, y_coords, marker='o')
plt.colorbar(label='Array Values')
plt.title('Array Visualization')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.grid(True)
plt.savefig("plt.jpg")



rnd = 10
for i, x in enumerate(stripe):
    if (i > round(rnd/2) + 1) and (i < len(stripe) - round(rnd/2) -1):
        tot = 0
        for j in range(i-round(rnd/2), i+round(rnd/2)):
            tot += x[-1]
        stripe[i].append(tot)
        tot = 0

    else:
        stripe[i].append(0)

stripe_sosssss = sorted(stripe, key=lambda x: x[-1], reverse=True)




def color_row_and_column_red(image_path, row_index, col_index, output_path):
    try:
        # Open the image using Pillow
        image = Image.open(image_path)

        # Get the image dimensions
        width, height = image.size

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Color the specified row in red
        for x in range(width):
            image.putpixel((x, row_index), (255, 0, 0))  # RGB value for red

        # Color the specified column in red
        for y in range(height):
            image.putpixel((col_index, y), (255, 0, 0))  # RGB value for red

        # Save the modified image
        image.save(output_path)
        print(f"Image saved with row {row_index} and column {col_index} colored red to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
output_image_path = "output_image.jpg"
row_to_color = mid
column_to_color = stripe_sosssss[0][-3]

color_row_and_column_red(image_path, row_to_color, column_to_color, output_image_path)


