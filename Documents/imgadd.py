import cv2 as cv
import numpy as np

gou  = cv.imread('./gou.jpeg')
print(gou.shape)

img = np.ones((1200,1600,3),np.uint8)*200
cv.imshow('orig',gou)
print(img.shape)

result = cv.add(gou,img)

cv.imshow('result',result)

cv.waitKey(0)
cv.destroyAllWindows()