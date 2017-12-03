"""
Detects objects with Haar-cascade detection
Author: Landon Wiedenman
"""

import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2

card_cascade = cv2.CascadeClassifier('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/cascade/cascade.xml')

img = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cards = card_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in cards:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

