import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
#blank[200:300, 300:400] = 0, 255, 0
#blank[:] = 0, 255, 0 #gleiche seitenverhältnisse
#cv.imshow('Green', blank)

# 2. Draw a Rectangle
#cv.rectangle(blank, (0,0), (250, 250), (200, 100, 200), thickness=2)
#cv.rectangle(blank, (250,250), (150, 350), (200, 100, 200), thickness=-1) #=cv.FILLED
#cv.imshow('rect', blank)

#blank.shape[0] ist die höher der zeichenfäche blank

# 3. Draw circle
#cv.circle(blank, (250, 250), 40, (0, 23, 160), thickness=3)
#cv.rectangle(blank, (249,251), (150, 350), (0,0,0), thickness=-1)
#cv.imshow('circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=2)
cv.imshow('circle', blank)

# 5. Write text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0))
cv.imshow('text', blank)


cv.waitKey(0)