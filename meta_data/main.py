from exif import Image

img_filename = 'image.jpg'
img_path = 'image.jpg'


with open(img_path, 'rb') as img_file:
    img = Image(img_path)

print(img.has_exif)

# Make of device which captured image
print(f'Make: {img.get("make")}')

# Model of device which captured image
print(f'Model: {img.get("model")}')

# Software involved in uploading and digitizing image
print(f'Software: {img.get("software")}')

# Name of photographer who took the image
print(f'Artist: {img.get("artist")}')

# Original datetime that image was taken (photographed)
print(f'DateTime (Original): {img.get("datetime_original")}')

# Details of flash function
print(f'Flash Details: {img.get("flash")}')

with open(f'modified_{img_filename}', 'wb') as new_image_file:
    new_image_file.write(img.get_file())
