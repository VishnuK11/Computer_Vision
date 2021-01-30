'''
Edge Detection
Laplacian
Sobel
Canny
'''

import os 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'cat2.jpeg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Laplace Method for Edge Detection
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# Sobel Filter
sobel_x = cv.Sobel(gray,cv.CV_64F, 1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F, 0,1)
cv.imshow('Sobel X',sobel_x)
cv.imshow('Sobel Y',sobel_y)

combine_sobel = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('Sobel X+Y',combine_sobel)

# Canny Edges - Multistage process
canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)