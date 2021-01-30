'''
HAAR Cascade
Single Face Test
Multi Face Test

'''

import os 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

dir_path = os.getcwd()+'/data/images/'
dir_face = os.getcwd()+'/data/face_recognition/'

# Use this for single face test
# img=cv.imread(dir_path+'Gal_gadot.jpeg')
# cv.imshow('Actress',img)

# Use this for multi face test
img=cv.imread(dir_path+'group2.jpeg')
cv.imshow('Marvel',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier(dir_face+'face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 6)

print('Number of faces is ',len(faces_rect))

for (x,y,w,h) in faces_rect:
	cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('Face',img)
cv.waitKey(0)
