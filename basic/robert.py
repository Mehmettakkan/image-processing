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

# Convert to RGB format (for compatibility with Matplotlib)
RGBImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale format
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Robert kernels for edge detection
kernelx = np.array([[-1, 0],[0, 1]], dtype = int)
kernely = np.array([[0, -1],[1, 0]], dtype = int)

# Filtering for edge detection
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

# Get absolute value
absx = cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)

# Get Robert edge detection result
Robert = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

# Lists containing titles and images are created.
Titles = ["Original","Robert"]
images = [RGBImage, grayImage]

# Displays images on the screen using Matplotlib.
for i in range(2):
    plt.subplot(1, 2, i+1),
    plt.imshow(images[i], "gray"),
    plt.xticks([]), # close labels of x axis
    plt.yticks()    # turn off y-axis labels
plt.show()  # Show entire chart







