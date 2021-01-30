'''
Threshold
Simple
Adaptive Gaussian
Adaptive Mean
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

# Simple Thresholding
#Other otpions: cv.THRESH_BINARY_INVERSE
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)

# Adaptive Thresholding
#Other otpions: cv.ADABTIVE_BINARY_MEAN
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Threshold',adaptive_thresh)

print(threshold,thresh	)

cv.waitKey(0)