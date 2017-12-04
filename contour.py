"""
Detects and draws contours on images
Author: Landon Wiedenman
"""

import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
import numpy as np
from matplotlib import pyplot as plt


# TODO: Finish this
def contour_image(image_path):
    """ Finds contours within an image """


    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    plt.imshow(img), plt.show()


