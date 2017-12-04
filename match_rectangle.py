"""
Detects rectangles in an image
Author: Landon Wiedenman
"""

import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/rectangle.jpg', 0)
img2 = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png', 0)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
image, contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)

plt.imshow(img), plt.show()