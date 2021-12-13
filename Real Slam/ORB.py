import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1 = cv.imread('Data/1.png',0)
img2 = cv.imread('Data/2.png',0)

# Locate features
# Initiate ORB detector
orb1 = cv.ORB_create()
orb2 = cv.ORB_create()
# find the keypoints with ORB
kp1 = orb1.detect(img1,None)
kp2 = orb2.detect(img2,None)
# compute the descriptors with ORB
kp1, des1 = orb1.compute(img1, kp1)
kp2, des2 = orb2.compute(img2, kp2)
# draw only keypoints location,not size and orientation
img1 = cv.drawKeypoints(img1, kp1, None, color=(0,255,0), flags=0)
img2 = cv.drawKeypoints(img2, kp2, None, color=(0,255,0), flags=0)


# FLANN parameters
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = cv.DrawMatchesFlags_DEFAULT)

img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

cv.imshow("Keypoints", img1)
cv.imshow("Keypoints2", img2)
cv.imshow("Matching", img3)
cv.waitKey(0)