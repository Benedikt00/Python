import cv2 as cv

#img = cv.imread('pictures/cat_large.jpg')
#cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)



capture = cv.VideoCapture('videos/dog.mp4')

while True:
    #images and vids
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()