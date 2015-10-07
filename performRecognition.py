# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

# Load the classifier
clf = joblib.load("digits_cls.pkl")

# Read the input image 
im = cv2.imread("asg_tag.jpg")

im = im[780:825, 895:935]
# im = im[780:825, 945:985]
# im = im[780:825, 995:1035]

# WebCam
# im = im[268:283, 233:257]
# im = im[275:293 , 302:328]
# im = im[275:293 , 270:293]

# cv2.imshow("Resulting Image with Rectangular ROIs", im)
# cv2.waitKey()

# Convert to grayscale and apply Gaussian filtering
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

for i in xrange(len(im_gray)):
    for j in xrange(len(im_gray[i])):
        if(im_gray[i][j] > 100):
            im_gray[i][j] = 255
        else:
            im_gray[i][j] = 0

blank_image = np.zeros((200, 200, 3), np.uint8)
blank_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)

for k in xrange(len(blank_image)):
    for l in xrange(len(blank_image[k])):
        blank_image[k][l] = 255

for k in xrange(len(im_gray)):
    for l in xrange(len(im_gray[k])):
        blank_image[k+80][l+80] = im_gray[k][l]

# cv2.imshow("Resulting Image with Rectangular ROIs", im_gray)
# cv2.waitKey()

# Threshold the image
ret, im_th = cv2.threshold(blank_image, 90, 255, cv2.THRESH_BINARY_INV)

# Find contours in the image
ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get rectangles contains each contour
rects = [cv2.boundingRect(ctr) for ctr in ctrs]

# For each rectangular region, calculate HOG features and predict
# the digit using Linear SVM.

digits = []

for rect in rects:
    # Draw the rectangles
    cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    # Make the rectangular region around the digit
    leng = int(rect[3] * 1.6)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
    # Resize the image
    roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
    roi = cv2.dilate(roi, (3, 3))
    # Calculate the HOG features
    roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
    # cv2.putText(blank_image, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
    digits.append(str(int(nbr[0])))

print digits
cv2.imshow("Resulting Image with Rectangular ROIs", blank_image)
cv2.waitKey()