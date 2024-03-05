#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:06:29 2023

@author: mehmetakkan
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np

# File path of the image to be processed.
path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/cup.png"

# Loads the image from the specified file path with OpenCV.
image = cv2.imread(path)

# Saves the uploaded image to a file named "cupKopy.png".
cv2.imwrite("cupKopy.png",image)

# Reduces the image by a certain factor.
half = cv2.resize(image, (0, 0), fx=0.1,fy=0.1)

# Enlarges the image by a specified factor.
bigger = cv2.resize(image,(1050, 1610), fx=0.1,fy=0.1)

# Stretches the image to a specific size, but uses a different interpolation method (cv2.INTER_NEAREST).
stretch_near = cv2.resize(image, (780, 540), interpolation = cv2.INTER_NEAREST)

# Lists containing titles and images are created.
Titles = ["Original", "Half","Bigger","cv2.INTER_NEAREST"]
images = [image, half, bigger, stretch_near]

# Total number of images.
count = 4

# Displays images on the screen using Matplotlib.
for i in range(count):
    plt.subplot(2, 2, i+1) # Creates a 2x2 subplot and places each image.
    plt.title(Titles[i])  # Determines the image title.
    plt.imshow(images[i]) # Displays the image on the screen.
plt.show() # Displays the window containing all images.