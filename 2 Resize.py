'''
Resize Images
Change Resolution of Video
'''

import os 
import cv2 as cv

dir_path = os.getcwd()+'/data/images/'
img=cv.imread(dir_path+'cat.jpeg')
cv.imshow("Cat",img)

def rescale(frame,scale=0.75):
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	dimensions=(width,height)
	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# For Live Video use this
def changeRes(width,height):
	capture.set(3,width) 
	capture.set(4,height)


capture=cv.VideoCapture(dir_path+"dog.mp4")
while True:
	try:
		isTrue,frame=capture.read()
		frame_resize=rescale(frame,scale=0.25)
		cv.imshow("dog scale",frame_resize)

		if cv.waitKey(1,) & 0xFF==ord('d'):	
			break
	except:
		break

capture.release()
cv.destroyAllWindows()