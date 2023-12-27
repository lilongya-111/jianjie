import cv2 as cv
import numpy as np
def callback():
    pass
cv.namedWindow('trackbar',cv.WINDOW_NORMAL)
cv.createTrackbar('R','trackbar',0,255,callback)
cv.createTrackbar('G','trackbar',0,255,callback)
cv.createTrackbar('B','trackbar',0,255,callback)

image = np.zeros((480,640,3),np.uint8)
while True:
    cv.imshow('trackbar',image)
    r=cv.getTrackbarPos('R','trackbar')
    g=cv.getTrackbarPos('G','trackbar')
    b=cv.getTrackbarPos('B','trackbar')
    image[:] = [b,g,r]
    cv.imshow('trackbar',image)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows

