'''
Read Images and Video
'''
import os 
import cv2 as cv

dir_path = os.getcwd()+'/data/images/'

# Read Image
img=cv.imread(dir_path+'cat.jpeg')
cv.imshow("Picture",img)
cv.waitKey(2000)

# Read Video
Vid=cv.VideoCapture(dir_path+'dog.mp4')
while True:
	isTrue,frame=Vid.read()

	try:
		
	# except:
		cv.imshow('Video',frame)
		if cv.waitKey(20) & 0xFF==ord('d'):
			break
	except:
		break
Vid.release()
cv.destroyAllWindows()

