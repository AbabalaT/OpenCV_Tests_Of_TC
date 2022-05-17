import numpy as np
import cv2
img1 = cv2.imread('11.jpg')#读取
img2 = cv2.imread('10.jpg')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)#转化
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
z=0 #纵坐标
h=0 #横坐标
while(z<=3999):
    h=0
    while(h<=2999):
        if(abs(img2[z,h,2]-128)<=abs(img1[z,h,2]-128)):
            img1[z,h]=img2[z,h]
        h=h+1
    z=z+1
    if(z%100==0):
            print(z)
img1=cv2.cvtColor(img1,cv2.COLOR_HSV2BGR)
cv2.imwrite('11.jpg',img1)


#abs(img2[z,h,2]-128)<=abs(img1[z,h,2]-128)
#img2[z,h,1]>=img1[z,h,1]
