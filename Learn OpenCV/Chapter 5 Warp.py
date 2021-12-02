# Warping perspective
import cv2
import numpy as np

img = cv2.imread("Learn OpenCV/Resources/chess.png")

width,height = 250,250

# create an array of floats for the corners of the chessboard
pts1 = np.float32([[69,83], [245,51], [136,230], [368,143]])
# create an array of the points that the corners are mapped to on the warped image
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
# create the transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# apply the transformation
imgOutput = cv2.warpPerspective(img, matrix, [width,height])


cv2.imshow("Image", img)
cv2.imshow("Warped Image", imgOutput)
cv2.waitKey(0)