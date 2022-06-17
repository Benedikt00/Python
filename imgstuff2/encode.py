from PIL import Image

def s_to_bitlist(s):
    ords = (ord(c) for c in s)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    return [(o >> shift) & 1 for o in ords for shift in shifts]

sth = "some"

strbyts = s_to_bitlist(sth)

print(strbyts)

for x in range(len(strbyts)):
    byte = strbyts[x]
    if byte == 1:
        strbyts[x] = 5

print(strbyts)

im = Image.open('image.jpg') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over

pichight = im.size[1]
piclenght = im.size[0]

rowrgb = []

for pixel in range(piclenght):
    nextrgb = pix[pixel, 1]
    rowrgb.append(nextrgb)

for x in range(len(strbyts)):
    rgbval = list(rowrgb[x])
    rgb = rowrgb[x][len(rowrgb[x]) - 1] #get last element of list[x]
    rgb = str(rgb)
    #print(strbyts[x])
    rgb = rgb.replace(rgb[len(rgb)-1], str(strbyts[x]))
    rgbval[len(rgbval)-1] = int(rgb)
    print(rgbval)
    rowrgb[x] = tuple(rgbval)

for i in range(len(strbyts)):
    print(str(rowrgb[i]) + str(strbyts[i]))

for x in range(len(strbyts)):
    pix[x, 1] = rowrgb[x]

im.save('returnimg.jpg', quality=95)
