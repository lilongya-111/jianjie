import cv2
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
image = cv2.imread('/home/longyali/Pictures/puke.png')


while True:

    cv2.imshow('image',image)
    key = cv2.waitKey(0)
    if(key &0xFF == ord('q')):
        break
    elif(key&0xFF==ord('s')):
        cv2.imwrite("/home/longyali/Pictures/puke2.jpeg",image)
    else:
        print(key)
        
cv2.destroyAllWindows()

