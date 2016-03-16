# digitRecognition

Code for digit recognition in python.  
Divided in two files:  
1. To generate the SVM classifier  
2. To perform digit recognition  

To generate the classifier -  
```
python generateClassifier.py
```
This downloads handwritten digits data from [mldata.org](http://www.mldata.org) and trains a linear SVM with it, and generates a classifier i.e. `digits_cls.pkl`  

The `performRecognition.py` script loads the classifier from the `digits_cls.pkl` file and uses it to classify digits in any given image.  
During its development, I had hardcoded the digit co-ordinates for testing purposes. Not much development has happened after that.  
I encourage you to give it a try.

#faceDetection

A simple code for face detection.