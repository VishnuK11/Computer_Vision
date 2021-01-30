'''
Image Transformations
1 Translate
2 Rotate
3 Resize
4 Flip
'''
import os 
import cv2 as cv
import numpy as np 

dir_path = os.getcwd() + '/data/images/'

img=cv.imread(dir_path+'cat.jpeg')
cv.imshow('Original cat',img)

# x -->right
# y -->down
# -x -->left
# -y -->up

# Translation
def translate(img,x,y):
	transMat=np.float32([[1,0,x],[0,1,y]])
	dimensions= (img.shape[1],img.shape[0])
	return cv.warpAffine(img,transMat,dimensions)

# Rotation
def rotate(img,angle,rotatePoint=None):

	height,width=img.shape[:2]

	if rotatePoint is None:
		rotatePoint=(width/2,height/2)

	rotMat=cv.getRotationMatrix2D(rotatePoint,angle,1.0)
	dimensions= (width,height)
	return cv.warpAffine(img,rotMat,dimensions)


# Translate
translated=translate(img,100,100)
cv.imshow('Translated',translated)

# Rotate
rotated=rotate(img,30)
cv.imshow('Rotate',rotated)

# Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Flip
# 0 is vertical flip, 1 is horizontal flip, -1 is both
flip=cv.flip(img,0)
cv.imshow('flip',flip)

cv.waitKey(0)