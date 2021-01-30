'''
Splitting and merging Color Channels
'''
import os 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'flower.jpeg')
blank =np.zeros((img.shape[0],img.shape[1]),dtype='uint8')

b,g,r=cv.split(img)

# Individual channels in Gray
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape,b.shape,g.shape,r.shape,blank.shape)

merge=cv.merge([b,g,r])
cv.imshow('Merged Image',merge)

# Individual channels in Respective Colors
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

cv.waitKey(0)
