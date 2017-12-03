"""
Detects objects with Haar-cascade detection
Author: Landon Wiedenman
"""

import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2

face_cascade = cv2.CascadeClassifier('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/training/cascade/cascade.xml')
# eye_cascade = cv2.CascadeClassifier('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/face_detection/haarcascade_eye.xml')

img = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # for (ex, ey, ew, eh) in eyes:
    #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# """
# Detects faces in images with Haar-cascade detection
# Author: Landon Wiedenman
# """

# import sys
# sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
# import cv2

# face_cascade = cv2.CascadeClassifier('/Users/landonwiedenman/Documents/development_projects/landongw/face_detection/haarcascade_frontalface_default.xml')
# # eye_cascade = cv2.CascadeClassifier('/Users/landonwiedenman/Documents/development_projects/landongw/face_detection/haarcascade_eye.xml')

# img = cv2.imread('/Users/landonwiedenman/Documents/development_projects/landongw/face_detection/images/6186697.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     # eyes = eye_cascade.detectMultiScale(roi_gray)
#     # for (ex, ey, ew, eh) in eyes:
#     #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()