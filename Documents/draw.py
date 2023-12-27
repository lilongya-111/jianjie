import cv2 as cv
import numpy as np
img = np.zeros((480,640,3),np.uint8)
cv.line(img,(10,20),(200,400),(0,0,255),5,4)
cv.line(img,(30,20),(300,400),(0,0,255),5,16)

cv.rectangle(img,(10,10),(100,100),(0,0,255),-1)

cv.circle(img,(320,240),100,(0,0,255))
cv.circle(img,(320,240),5,(0,0,255),-1)
cv.ellipse(img,(320,240),(100,50),0,0,360,(0,0,255))
pts = np.array([(300,10),(150,100),(450,100)],np.int32)
cv.polylines(img,[pts],True,(0,0,255))
cv.fillPoly(img,[pts],(255,255,0))
cv.putText(img,"Hello World!",(10,400),cv.FONT_HERSHEY_PLAIN,2,(255,0,0))
cv.imshow('draw',img)
cv.waitKey(0)
cv.destroyAllWindows()