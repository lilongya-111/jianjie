import cv2 as cv
import numpy as np
a = np.array([1,2,3])
print(a)
print()
b = np.array([[1,2,3],[4,5,6]])
print(b)
print()

c = np.zeros((2,10,10),np.uint8)
print(c)
print()
d = np.ones((2,8,8),np.uint8)
print(d)
print()
e = np.full((8,8),41,np.uint8)
print(e)
print()
f = np.identity(9)
print(f)
print()
g = np.eye(5,7,k=1)
print(g)
image = np.zeros((480,640,3),np.uint8)

print(image[100,100])
count = 0
while count < 200 :
    image[count,100,1] = 255
    count = count +1

roi = image [100:400,100:600]
roi[:,:] = [0,0,255]
roi[10:200,10:200] = [0,255,0]

cv.imshow('image',image)    
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows