# Contour detection

import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    

path = "Learn OpenCV/Resources/shapes.png"
img = cv2.imread(path)

imgBlack = np.zeros(img.shape)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

imgGray3 = np.stack([imgGray,imgGray,imgGray],axis=-1) # Put the grayscale images in a BGR matrix format
imgBlur3 = np.stack([imgBlur,imgBlur,imgBlur],axis=-1)
imgCanny3 = np.stack([imgCanny,imgCanny,imgCanny],axis=-1)
tot1 = np.hstack((img,imgGray3,imgBlur3))
tot2 = np.hstack((imgCanny3, imgBlack, imgBlack))


cv2.imshow("Original", tot1)
cv2.imshow("Gray", tot2)

cv2.waitKey(0)