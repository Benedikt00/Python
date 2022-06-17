import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

def s_to_bitlist(s):
    ords = (ord(c) for c in s)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    return [(o >> shift) & 1 for o in ords for shift in shifts]

img = Image.open("image2.jpg")
arr = np.array(img)

height, width = img.size

max = math.floor(width/8)

toLong = True

while toLong:
    sth = input(f"Gib deine Nachricht ein (max {max} Zeichen): ")
    if len(sth)*8 < width:
        toLong = False
    else:
        print("Your message is to long, try again")

strbyts = s_to_bitlist(sth)


rowrgb = []

row = 0

for pixel in range(len(strbyts)):
    nextrgb = arr[pixel, row]
    rowrgb.append(nextrgb)

row = 0

for x in range(len(strbyts)):
    rgbval = list(rowrgb[x])
    rgb = rowrgb[x][len(rowrgb[x]) - 1]
    rgb = str(rgb)
    rgb = rgb.replace(rgb[len(rgb)-1], str(strbyts[x]))
    rgbval[len(rgbval)-1] = int(rgb)
    rowrgb[x] = rgbval

for x in range(len(strbyts)):
    arr[x, 1] = rowrgb[x]

plt.imsave('output.png', arr.astype(np.uint8))
