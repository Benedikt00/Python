from PIL import Image

im = Image.open('returnimg.jpg') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over

pichight = im.size[1]
piclenght = im.size[0]

rowrgb = []

for pixel in range(piclenght):
    nextrgb = pix[pixel, 1]
    rowrgb.append(nextrgb)

for x in range(100):
    print(rowrgb[x])






