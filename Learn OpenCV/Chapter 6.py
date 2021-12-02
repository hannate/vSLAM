# Joining Images
import cv2
import numpy as np

img = cv2.imread("Learn OpenCV/Resources/mandelbrot.png")

hor = np.hstack((img,img)) # I flex taped these matrices together!
ver = np.vstack((img,img)) # Images do have to be the same format and size

cv2.imshow("Horizontally Stacked", hor)
cv2.imshow("Vertically Stacked", ver)
cv2.waitKey(0)