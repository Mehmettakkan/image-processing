#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:23:45 2024

@author: mehmetakkan
"""

# Import necessary libraries
import cv2  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations and array manipulation
import matplotlib.pyplot as plt  # Matplotlib for plotting images

# Specify the path to the fingerprint image
path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/finger_print.png"

# Load the image using OpenCV
image = cv2.imread(path)

# Create a 5x5 kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Apply erosion to the image
img_erosion = cv2.erode(image, kernel, iterations=1) #iteration parameters specify how many times the process will be repeated.
# Erosion shrinks the brighter regions (foreground) of the image, often used for:
# - Removing small, unwanted details
# - Separating connected objects
# - Thinning edges

# Apply dilation to the image
img_dilation = cv2.dilate(image, kernel, iterations=1)
# Dilation expands the brighter regions (foreground), often used for:
# - Filling in gaps
# - Connecting broken parts of objects
# - Enhancing edges

# It is used to remove noise and small blemishes, it is used in the etching process, 
#which is etching followed by expansion.
openinig = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# It performs capping, which is expansion followed by etching, 
#and is often used to fill small holes and gaps.
closig = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Calculates the morphological gradient by highlighting edges and boundaries in the image.
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Prepare titles and images for display
Titles = ["Original", "Erosion", "Dilation"]
imgs = [image, img_erosion, img_dilation]

# Create a 1x3 subplot for displaying the images
count = 3
for i in range(count):
    plt.subplot(1, 3, i + 1)  # Create a subplot at position i+1
    plt.title(Titles[i])  # Set the title
    plt.imshow(imgs[i])  # Display the image

# Show the plot
plt.show()


Titles = ["Original", "Openinig", "Closig", "Gradient"]
imgs = [image, openinig, closig, gradient]


count = 4
for i in range(count):
    plt.subplot(1, 4, i + 1)
    plt.title(Titles[i])
    plt.imshow(imgs[i])

plt.show()










