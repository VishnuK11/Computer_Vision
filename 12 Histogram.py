'''
Histogram
'''
import os 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'cat2.jpeg')
cv.imshow('Cat',img)

# 1 BGR to GRAY
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# # 1.1 Grayscale Histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

# 1.2 Mask + Grayscale Histogram
blank = np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank,(img.shape[1]/2,img.shape[0]/2),100,255,-1)
mask=cv.bitwise_and(img,img,mask=circle)
gray_hist = cv.calcHist([gray],[0],circle,[256],[0,256])
cv.imshow('Masked',mask)

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


# 2.1 Mask + Color Histogram
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim([0,256])

colors=['b','g','r']
for i,col in enumerate(colors):
	hist=cv.calcHist([img],[i],None,[256],[0,256])
	plt.plot(hist,color=col)
	plt.xlim([0,256])
plt.show()

cv.waitKey(0)