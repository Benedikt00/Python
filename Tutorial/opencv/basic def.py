import cv2 as cv

img = cv.imread('pictures/park.jpg')

cv.imshow('Cat', img)

# converting to grayscale

#gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
#cv.imshow('grea', gray)


# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)


# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Dilating the image
dil = cv.dilate(canny, (10, 10), iterations=3)
cv.imshow('dil', dil)

# Eroding
eroded = cv.erode(dil, (10, 10), iterations=3)
cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('sth', resized)

#croping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)