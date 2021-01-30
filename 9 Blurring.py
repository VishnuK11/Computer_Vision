'''
Read Images and Video
'''
import os 
import cv2 as cv
import numpy as np 

dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'cat.jpeg')
cv.imshow('Cat',img)

# Average Blur 
avg=cv.blur(img,(7,7))
cv.imshow('Average',avg)

# Guassian Bllur
gaussian=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Guassian',gaussian)

# Median Blur
median=cv.medianBlur(img,7,1)
cv.imshow('Median',median)

# BiLateral Blur
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)