import numpy as np
import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create SURF object
surf = cv2.xfeatures2d.SURF_create()
surf.setHessianThreshold(45000)

kp, des = surf.detectAndCompute(img, None)
print("Keypoints: ", len(kp))

img = cv2.drawKeypoints(gray, kp, None)
cv2.imwrite('surf_keypoints.jpg', img)

# Recompute the feature points and draw it
kp = surf.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2), plt.show()
