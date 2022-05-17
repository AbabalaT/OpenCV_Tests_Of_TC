import numpy as np
import cv2
img1 = cv2.imread('05.jpg')#读取
img2 = cv2.imread('10.jpg')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)#转化
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
