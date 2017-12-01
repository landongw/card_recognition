"""
Detects and draws contours on images
Author: Landon Wiedenman
"""

import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
import numpy as np
# import RGB_slider

# TODO: Finish this
def contour_image():
    """ Finds contours within an image """
    
    img = cv2.imread('images/cards_bw.jpg', 0)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy, _ = cv2.findContours(thresh, 1, 2)

    cnt = contours[0]
    M = cv2.moments(cnt)
    print(M)
    cv2.imshow('cards_bw', img)
    # print(cnt)
    # RGB_slider.image_slider() // Cool color slider

    # centroid
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print(cx)
    print(cy)

    # contour area
    area = cv2.contourArea(cnt)

    # contour perimeter
    perimeter = cv2.arcLength(cnt, True)
    print(perimeter)