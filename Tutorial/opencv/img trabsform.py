import cv2 as cv
import numpy as np

img = cv.imread('pictures/park.jpg')

cv.imshow('Cat', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = [img.shape[1], img.shape[0]]
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translate = translate(img, 100, 100)
cv.imshow('Translate', translate)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = [width//2, height//2]

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotate = rotate(img, 45)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('res',resized)

cv.imshow('sth', rotate)

#flipping
flip = cv.flip(img, 0)
#0 = vertical
#1 = horizontal
#-1 = beides

cv.imshow('flip', flip)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.imshow('cropped', cropped)

cv.waitKey(0)