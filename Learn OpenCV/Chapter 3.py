import cv2
import numpy as np

img = cv2.imread("Learn OpenCV/Resources/chess.png")
print(img.shape)

imgResize = cv2.resize(img, (200, 200)) # width then height

imgCropped = img[0:200,200:400] # height then width

cv2.imshow("Image",img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)