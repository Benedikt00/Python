import numpy as np
from PIL import Image

img1 = Image.open("P1.JPG")
arr1 = np.array(img1)

height_1, width_1 = img1.size

img2 = Image.open("P2.JPG")
arr2 = np.array(img2)

height_2, width_2 = img2.size

edge1 = []

for i in range(height_1):
	edge1.append(arr1[i][-1])



