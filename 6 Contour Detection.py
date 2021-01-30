'''
Contour Detection
'''
import os 
import cv2 as cv
import numpy as np 

dir_path = os.getcwd()+'/data/images/'

img=cv.imread(dir_path+'flower.jpeg')
cv.imshow('Orignal cat',img)

blank=np.zeros((img.shape),dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 1 Canny Edges
canny=cv.Canny(gray,125,175)
cv.imshow('Canny',canny)

# 1.1 Blur
blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
blur=cv.Canny(blur,125,175)
cv.imshow('Blur Canny',blur)

# 2 Thresholding
ret,thresh= cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours),' contours found:')

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('Contours',blank)
cv.waitKey(0)

