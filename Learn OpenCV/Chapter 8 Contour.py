# Contour detection

import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCorner = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            
            objectType = {
                3:"Tri",
                4:"Square",
                5:"Pentagon",
                6:"Hexagon",
                7:"Heptagon",
                8:"Octagon",
                9:"Nonagon",
                10:"Decagon"
            }

            objTypeName=objectType.get(objCorner, "")
            if objCorner > 10:
                objTypeName = "Circle"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour, objTypeName, (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),2)

path = "Learn OpenCV/Resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgCopy = img.copy()

imgBlack = np.zeros(img.shape)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0.65)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgGray3 = np.stack([imgGray,imgGray,imgGray],axis=-1) # Put the grayscale images in a BGR matrix format
imgBlur3 = np.stack([imgBlur,imgBlur,imgBlur],axis=-1)
imgCanny3 = np.stack([imgCanny,imgCanny,imgCanny],axis=-1)

tot1 = np.hstack((img,imgGray3,imgBlur3))
tot2 = np.hstack((imgCanny3, imgContour, imgCopy))


cv2.imshow("Original", tot1)
cv2.imshow("Gray", tot2)

cv2.waitKey(0)