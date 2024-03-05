#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:36:41 2023

@author: mehmetakkan
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np

# File path of the image to be processed.
path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg"

# Loads the image from the specified file path with OpenCV.
image = cv2.imread(path)

# Sets the threshold value. This value determines whether pixels are classified as black or white.
thresh = 100

# Sets pixels above the specified threshold to white (255) and those below to black (0).
ret, thresh1 = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)

# Sets pixels above the specified threshold to white (255) and those below to black (0), but inverts.
ret, thresh2 = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY_INV)

# Leaves pixels above the specified threshold white (255) and those below the same.
ret, thresh3 = cv2.threshold(image, thresh, 255, cv2.THRESH_TRUNC)

# Sets pixels above the specified threshold value to white (255) and those below it to black (0).
ret, thresh4 = cv2.threshold(image, thresh, 255, cv2.THRESH_TOZERO)

# Leaves pixels above the specified threshold value unchanged and sets those below to black (0).
ret, thresh5 = cv2.threshold(image, thresh, 255, cv2.THRESH_TOZERO_INV)

# Displays thresholded images on the screen.
# cv2.imshow("THRESH_BINARY",thresh1)
# cv2.imshow("THRESH_BINARY_INV",thresh2)
# cv2.imshow("THRESH_TRUNC",thresh3)
# cv2.imshow("THRESH_TOZERO",thresh4)
# cv2.imshow("THRESH_TOZERO_INV",thresh5)

# Lists containing titles and images are created.
Titles = ["Original", "THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]

# Total number of images.
count = 6

# Displays images on the screen using Matplotlib.
for i in range(count):
    plt.subplot(3, 3, i+1) # Creates a 3x3 subplot and places each image.
    plt.title(Titles[i])  # Determines the image title.
    plt.imshow(images[i]) # Displays the image on the screen.
plt.show() # Displays the window containing all images.








