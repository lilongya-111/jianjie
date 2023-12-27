import cv2 as cv
import numpy as np
img =np.zeros((480,640,3),np.uint8)
curshape =0
startpos =(0,0)
def mouse_callback(event,x,y,flags,userdata):
    global curshape,startpos

    #print( event,x,y,flags,userdata)
    if(event & cv.EVENT_LBUTTONDOWN == cv.EVENT_LBUTTONDOWN):
        startpos =(x,y)
    elif (event &cv.EVENT_LBUTTONUP == cv.EVENT_LBUTTONUP):
        if curshape ==0 :
            cv.line(img,startpos,(x,y),(0,0,255))
        elif curshape ==1:
            cv.rectangle(img,startpos,(x,y),(0,0,255))
        elif curshape == 2:
            a = (x-startpos[0])
            b = (y-startpos[1])
            r = int((a**2+b**2)**0.5)
            cv.circle(img,startpos,r,(0,0,255))
        else:
            print('error:no shape')
cv.namedWindow('drawshape',cv.WINDOW_NORMAL)
cv.setMouseCallback('drawshape',mouse_callback)   
while True:
    cv.imshow('drawshape',img)
    key =cv.waitKey(1)& 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):
        curshape = 0
    elif key == ord('r'):
        curshape = 1
    elif key == ord('c'):
        curshape = 2


cv.destroyAllWindows()