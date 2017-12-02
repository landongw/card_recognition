"""
Runs the card recognition application
Author: Landon Wiedenman
"""

from contour import contour_image
from corner_detection import detect_corner
from train_find_image import find_image
# import RGB_slider


def main():
    """ Runs the program """

    # Find image within another image
    find_image('images/sevenhearts.png', 'images/cards.png')

    # Corner detection
    detect_corner('images/cards.png')

    # TODO: Find contours in image and show
    # contour_image()

if __name__ == "__main__":
    main()
