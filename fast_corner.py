import numpy as np
import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png')

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector()

# find and draw the keypoints
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))

# Print all default params
print("Threshold: ", fast.getInt('threshold'))
print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
print("neighborhood: ", fast.getInt('type'))
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imwrite('fast_true.png', img2)

# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression', 0)
kp = fast.detect(img, None)  # TODO: Figure out why this doesn't work

print("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))

cv2.imwrite('fast_false.png', img3)