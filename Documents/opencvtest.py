import cv2
import numpy as np

# 读取图像
image = cv2.imread('/home/longyali/Pictures/opencv.png')

# 显示图像
#cv2.imshow('Original Image', image)
print(image.shape)
cv2.imshow("blue",image[:,:,0])
cv2.imshow("green",image[:,:,1])
cv2.imshow("red",image[:,:,2])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,500,0.1,10)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(image,(int(x),int(y)),3,(255,0,255),-1)

cv2.imshow("gray",gray)
crop = image[0:300,0:300]
cv2.imshow("crop",crop)

image = np.zeros([300,300,3],dtype=np.uint8)
cv2.line(image,(100,200),(250,250),(255,0,0),3)
cv2.rectangle(image,(30,100),(60,150),(0,255,0),3)
cv2.circle(image,(150,100),20,(0,0,250),3)
cv2.putText(image,"hello",(100,50),0,1,(255,255,255))
cv2.imshow("image",image)




# 让我们使用新的宽度和高度缩小图像
# down_width = 300
# down_height = 200
# down_points = (down_width, down_height)
# resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

# # 让我们使用新的宽度和高度来增加图像尺寸
# up_width = 600
# up_height = 400
# up_points = (up_width, up_height)
# resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)

# # 显示图像
# #cv2.imshow('Resized Down by defining height and width', resized_down)

# #cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey()

#按下任意键退出
cv2.destroyAllWindows()
