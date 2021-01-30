'''
Functions Covered:
1 Change colors
2 Blur
3 Edge Cascade
4 Dilating
5 Eroding
6 Resizing
7 Crop
'''

import os 
import cv2 as cv

dir_path = os.getcwd()+'/data/images/'

img=cv.imread(dir_path+'cat.jpeg')
cv.imshow('Original',img)

# 1 GrayScale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GreyCat',gray)

# # 2 Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blurred_Cat',blur)

# 3 Edge Cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edge',canny)

# 4 Dilating the image
dilated= cv.dilate(canny,(3,3),iterations=3)
cv.imshow('Dilated Edge',dilated)

# 5 Eroding
eroded= cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded Edge',eroded)

# 6 Resize
resize= cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resize)

# 7 Crop
cropped=img[50:200,100:200]
cv.imshow('Croped',cropped)
print(img.shape)


cv.waitKey(0)