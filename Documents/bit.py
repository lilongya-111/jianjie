import cv2 as cv
import numpy as np

img = np.ones((480,640),np.uint8)
img2= np.zeros((480,640),np.uint8)

img[50:150,50:150]=255
img2[20:120,20:120]=255
cv.imshow('img',img)

new_img = cv.bitwise_not(img)
new2_img = cv.bitwise_and(img,img2)
cv.imshow('new_img',new_img)
cv.imshow('new2_img',new2_img)
cv.waitKey(0)