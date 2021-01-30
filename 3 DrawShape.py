'''
Draw Shapes using CV
'''

import os 
import cv2 as cv

dir_path = os.getcwd()+'/data/images/'
import numpy as np 

# 1 Createa blank black image
blank=np.zeros((500,500,3))

# 2 Green rectangle filled
square=blank
square[200:300,100:400,1]=255

# 3 Green rectable with line thickness
# cv.rectangle(green,(0,0),(100,100),(0,255,0),thickness=2)
square=cv.rectangle(square,(0,0),(square.shape[0]/2,square.shape[1]/2),(0,255,0),thickness=cv.FILLED)

# 4 Draw cirle
cv.circle(square,(blank.shape[0]/2,blank.shape[1]/2),40,(0,0,255),thickness=-1)

# 5 Draw  a line:
cv.line(square,(0,0),(blank.shape[0]/2,blank.shape[1]/2),(0,0,255),thickness=1)

# 6 Write Text 
cv.putText(blank,"Hello World, How you doing?",(24,24),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow("Square",square) 
cv.waitKey(0)
