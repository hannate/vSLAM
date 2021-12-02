import cv2
import numpy as np

img = np.zeros((512, 512, 3),np.uint8) # Initialize a black image
#img[:]=255,0,0 # make it blue

# img.shape[1] is image width, img.shape[0] is image height
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 5) # src, start, end, color, thickness
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2) # Use cv2.FILLED for thickness for a solid shape. Note the BRG color order.
cv2.circle(img, (400, 50), 30, (255,255,0),5)

cv2.putText(img, "YO WASSUP", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 150,0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)