from PIL import Image

im = Image.open('returnnnnntest.png') # Can be many different formats.
pix = im.load()

rgb = pix[0, 0]

pix[0, 1] = (100, 100, 12, 1)

im.save('returnnnnntest.png')






