'''
Face Recogition Training
Load yml and npy files
Detect faces
Locate in image

Performance : 
Training Accuracy 100%
Testing Accuracy 28%
'''

import os 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

# Import all the directories needed
dir_path = os.getcwd()+'/data/images/'
dir_face = os.getcwd()+'/data/face_recognition/'
dir_train = os.getcwd()+'/data/face_recognition/train/'
dir_test = os.getcwd()+'/data/face_recognition/test/'

# Import the labels and people names
features = np.load(dir_face+'features.npy',allow_pickle=True)
labels = np.load(dir_face+'labels.npy',allow_pickle=True)
people =['Dicaprio','Tom','Natalie','Scarlett','Saoirse','Will','Beyonce']


# Face recognition function to predict a label and display it
def face_recognition(img):
	
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	
	# Load Face Recognizer
	face_recognizer = cv.face.LBPHFaceRecognizer_create()
	face_recognizer.read(dir_face+'face_trained.yml')
	
	# Detect a face and store R.O.I of Image
	haar_cascade = cv.CascadeClassifier(dir_face+'face.xml')
	faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 8)
	
	for (x,y,w,h) in faces_rect:
		faces_roi = gray[y:y+h,x:x+w]
		label, confidence = face_recognizer.predict(faces_roi)
	
		print('Label is ', people[label], 'with confidence ',confidence)
		cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
		cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
	
	cv.imshow('Face recognition',img)
	cv.waitKey(1000)	

listOfFiles = list()
for (dirpath, dirnames, filenames) in os. walk(dir_test):
	listOfFiles += [os.path. join(dirpath, file) for file in filenames]

for img in listOfFiles:
	img = cv.imread(img)
# img = cv.imread(dir_face+'test/ws_1.jpeg')
	face_recognition(img)		