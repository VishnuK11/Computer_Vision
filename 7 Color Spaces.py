'''
Color Spaces
BGR
HSV
LAB
RGB
'''
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt


dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'flower.jpeg')
cv.imshow('Flower',img)

# 1 BGR to GRAY
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2 BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# 3 BGR to L*A*B
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# 4 MATPLOTLIB IS RGB method
plt.imshow(img)
plt.show()

# 5 BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# plt.imshow(rgb)
# plt.show()

# 6 HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

# 7 LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR',lab_bgr)

cv.waitKey(0)
