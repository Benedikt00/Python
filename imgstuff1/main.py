from PIL import Image
import random
from expandation import *


value = (0, 0, 0)
randrowrgb = []


def check(list1, val):
    # traverse in the list
    for x in list1:

        # compare with all the values
        # with val
        if val >= x:
            return False
    return True


def erhoheUm1(list, listplace, jumpval):
    loc = list[listplace]
    bgthan = check(loc, jumpval)
    if not bgthan:
        loc = [x + 100 for x in loc]
        loc = tuple(loc)
    else:
        loc = [x - 100 for x in loc]
        loc = tuple(loc)

    return loc


im = Image.open('images/paint.jpg') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over

pichight = im.size[1]
piclenght = im.size[0]
randRow = random.randrange(2, pichight-1)
print(randRow)

for pixel in range(piclenght):
    nextrgb = pix[pixel, randRow]
    randrowrgb.append(nextrgb)

for x in range(piclenght):
    rgbval = erhoheUm1(randrowrgb, x, 155)
    pix[x,randRow + 1] = rgbval

liRandRow = list(str(randRow))

liRandRow = getrgbs(liRandRow)

cords = [[0, 0], [0, piclenght-1], [pichight-1, 0],[pichight-1, piclenght-1]]

for x in range(len(cords)):
    cordx = cords[x][0]
    cordy = cords[x][1]

    print(cordx)
    print(cordy)

    print(pix[cordx, cordy])


im.save('returntest.png')  # Save the modified pixels as .png