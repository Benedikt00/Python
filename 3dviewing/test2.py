from test import *
import numpy as np

def getSurfaceNormal(file):
    file = open(file) #open File
    lines = file.readlines()
    cords = []
    for i in lines:
        if "facet normal" in i: #leaves only the normals to use
            i = i[16:-2]
            i = i.split()
            cords.append(i)

    for i in range(len(cords)):
        for j in range(len(cords[i])):
            cords[i][j] = float(cords[i][j])

    return cords

print(getSurfaceNormal("cube.STL"))
    


