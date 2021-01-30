# Computer_Vision
This repository contains the concepts of Computer Vision from reading an image to detecting faces using Deep Learning.

# Intro to Computer Vision and OpenCV

1. [Read and Write](https://github.com/VishnuK11/Computer_Vision/blob/main/1%20Read%20Write.py)
2. [Resize](https://github.com/VishnuK11/Computer_Vision/blob/main/2%20Resize.py)
3. [Draw Shape](https://github.com/VishnuK11/Computer_Vision/blob/main/3%20DrawShape.py)
4. [Key Functions](https://github.com/VishnuK11/Computer_Vision/blob/main/4%20KeyFunctions.py)
5. [Transform](https://github.com/VishnuK11/Computer_Vision/blob/main/5%20Transform.py)
6. [Contour Detection](https://github.com/VishnuK11/Computer_Vision/blob/main/6%20Contour%20Detection.py)
7. [Color Spaces](https://github.com/VishnuK11/Computer_Vision/blob/main/7%20Color%20Spaces.py)
8. [Color Channels](https://github.com/VishnuK11/Computer_Vision/blob/main/8%20Color%20Channels.py)
9. [Blurring](https://github.com/VishnuK11/Computer_Vision/blob/main/9%20Blurring.py)
10. [BitWise Operations](https://github.com/VishnuK11/Computer_Vision/blob/main/10%20Bitwise.py)
11. [Masking](https://github.com/VishnuK11/Computer_Vision/blob/main/11%20Masking.py)
12. [Histogram](https://github.com/VishnuK11/Computer_Vision/blob/main/12%20Histogram.py)
13. [Threshold](https://github.com/VishnuK11/Computer_Vision/blob/main/13%20Threshold.py)
14. [Edge Detection](https://github.com/VishnuK11/Computer_Vision/blob/main/14%20Edge%20Detection.py)
15. [HAAR Cascade](https://github.com/VishnuK11/Computer_Vision/blob/main/15%20HAAR%20Cascade.py)

# Detecting Faces in OpenCV
16. Face Recognition
    -  [Face Train](https://github.com/VishnuK11/Computer_Vision/blob/main/16%20Face%20Train.py)
    -  [Face Recognition](https://github.com/VishnuK11/Computer_Vision/blob/main/16%20Face%20Recognition.py)
    
    HAAR Cascade was used to detect faces and locate regions of interest (ROIs). These ROIs were trained using the FaceRecognizer function of the OpenCv module for 7 classes/persons. The model performed with an accuracy of 100% on seen data and 28% on unseen data. 

# Face Recognition using Deep Learning
17. Deep Learning Face Recognition
    - [Simpsons Character Dataset](https://github.com/VishnuK11/Computer_Vision/blob/main/17%20Simpson-Character-Dataset.ipynb)
    
    Used the simpsons character dataset to train images using transfer learning from a model build upon an inception architecture. A subset of 8 classes and their corresponding data was used. The model was pretrained on the FaceNet database. 3 Additional dense layers that were added were trained on the dataset. The model performed with an accuracy of 86% on seen data and 83% on the test data.  
