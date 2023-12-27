import cv2 as cv
import numpy as np
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)

cv.namedWindow('mouse',cv.WINDOW_NORMAL)
cv.resizeWindow('mouse',640,480)
cv.setMouseCallback('mouse',mouse_callback,"123")
img = np.zeros((480,640,3),np.uint8)
while True:
    cv.imshow('mouse',img)
    key  = cv.waitKey(1)
    if key & 0xFF ==ord('q'):
        break

cv.destroyAllWindows