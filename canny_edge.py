import numpy as np
import sys
sys.path.append('/usr/local/Cellar/opencv/3.3.1_1/lib/python3.6/site-packages')
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/landonwiedenman/Documents/lc101/hacker-problems/card_recognition/images/cards.png')

edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()