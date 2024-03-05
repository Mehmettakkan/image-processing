#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:44:40 2023

@author: mehmetakkan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter

# Read the image
img = cv2.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/brain.jpg", cv2.COLOR_BGR2GRAY)

# Create a copy of the image in RGB format for Matplotlib compatibility
RGBImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create another copy of the image in grayscale format for edge detection
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Robert kernels for edge detection
kernelx = np.array([[-1, 0],[0, 1]], dtype = int) # Define horizontal kernel
kernely = np.array([[0, -1],[1, 0]], dtype = int) # Define vertical kernel

# Apply filtering for edge detection in x and y directions
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx) # Apply horizontal kernel
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely) # Apply vertical kernel

# Combine the absolute values to get the final Robert edge detection result
absx = cv2.convertScaleAbs(x)  # Absolute value of x
absy = cv2.convertScaleAbs(y)  # Absolute value of y

# Combine the absolute values to get the final Robert edge detection result
Robert = cv2.addWeighted(absx, 0.5, absy, 0.5, 0) # Combine with equal weights

# Lists containing titles and images are created.
Titles = ["Original","Robert"]
images = [RGBImage, grayImage]

# Displays images on the screen using Matplotlib.
for i in range(2):
    plt.subplot(1, 2, i+1),
    plt.imshow(images[i], "gray"), # Display the image in grayscale
    plt.xticks([]), # Turn off axis ticks for cleaner display
    plt.yticks()    
plt.show()  # Show entire chart







