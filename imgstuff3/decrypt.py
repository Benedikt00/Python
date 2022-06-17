import numpy as np
from PIL import Image

img = Image.open("output.png")
arr = np.array(img)

height, width = img.size


rowrgb = []

for pixel in range(width):
    nextrgb = arr[pixel, 1]
    nextrgb = nextrgb[:-1]
    rowrgb.append(nextrgb)

lastng = []

for el in range(len(rowrgb)):
    nextnum = rowrgb[el][len(rowrgb[el])-1]
    lastng.append(int(repr(nextnum)[-1]))

pos = -1

nowant = [2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(lastng)):

    if lastng[i] in nowant:
        pos = i
        break

print(pos)

prbin = lastng[0:pos]

print(prbin)

def bitlist_to_chars(bl):
    bi = iter(bl)
    bytes = zip(*(bi,) * 8)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    for byte in bytes:
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))

def bitlist_to_s(bl):
    return ''.join(bitlist_to_chars(bl))

print(bitlist_to_s(prbin))
