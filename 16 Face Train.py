'''
Face Recogition Training
Create a list of images to train
Detect a R.O.I - Region of Interest
Train it
Save classififier, features and labels
'''

import os 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

dir_path = os.getcwd()+'/data/images/'
dir_face = os.getcwd()+'/data/face_recognition/'
dir_train = os.getcwd()+'/data/face_recognition/train/'

people =['Dicaprio','Tom','Natalie','Scarlett','Saoirse','Will','Beyonce']

features = []
labels = []

haar_cascade = cv.CascadeClassifier(dir_face+'face.xml')

def create_train():
	for person in people:
		path = os.path.join(dir_train,person)
		label = people.index(person)

		for img in os.listdir(path):
			img_path=os.path.join(path,img)

			img_array = cv.imread(img_path)
			gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

			faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 8)

			for (x,y,w,h) in faces_rect:
				faces_roi = gray[y:y+h,x:x+w]
				cv.imshow('Print',faces_roi)
				cv.waitKey(20)
				
				features.append(faces_roi)
				labels.append(label)

create_train()

# cv.waitKey(0)
print(len(features),len(labels))

features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train the recognizer on the feature list and labels list
face_recognizer.train(features,labels)

face_recognizer.save(dir_face+'face_trained.yml')
np.save(dir_face+'features.npy',features)
np.save(dir_face+'labels.npy',labels)