'''
Masking
'''
import os 
import cv2 as cv
import numpy as np 

dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'cat.jpeg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# Mask
mask=cv.circle(blank,(img.shape[1]/2,img.shape[0]/2),40,255,-1)
cv.imshow('Mask',mask)

# Masked Image
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

# AND + MASK
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(130,100),90,255,-1)
new_mask=cv.bitwise_and(rectangle,circle)
new_masked=cv.bitwise_and(img,img,mask=new_mask)
cv.imshow('New Masked',new_masked)

cv.waitKey(0)