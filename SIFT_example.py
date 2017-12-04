import numpy as np
import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray, None)

img = cv2.drawKeypoints(gray, kp, None)
cv2.imwrite('sift_keypoints.jpg', img)

img = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('sift_keypoints.jpg', img)

kp, des = sift.detectAndCompute(gray, None)
