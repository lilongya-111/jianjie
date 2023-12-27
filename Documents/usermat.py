import cv2 as cv
import numpy as np

img =cv.imread('./puke.jpeg')

img2 = img

img3 =img.copy()

img [10:100,10:100] = [0,0,255]
cv.imshow('img',img)
cv.imshow('img2',img2)
cv.imshow('img3',img3)
cv.waitKey(0)
cv.destroyAllWindows