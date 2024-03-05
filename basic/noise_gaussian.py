#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:08:12 2023

@author: mehmetakkan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/brain.jpg"

image = cv2.imread(path)

# First Gaussian filter: Kernel size (3.3), standard deviation 0
blur1 = cv2.GaussianBlur(np.array(image), (3,3), 0)

# Second Gaussian filter: Kernel size (5.5), standard deviation 15
blur2 = cv2.GaussianBlur(np.array(image), (5,5), 10)

# Create a new figure in Matplotlib
plt.Figure(figsize = (15, 12))

# Select the first subgraph in a 1x3 subgraph layout
plt.subplot(131)
# Show original image
plt.imshow(image)
# Set the title of the selected subgraph
plt.title("Original")

# Select the second subgraph in a 1x3 subgraph layout
plt.subplot(132)

# Show the first Gaussian filtered image
plt.imshow(blur1)

# Set the title of the selected subgraph
plt.title("Blur1")

# Select the third subgraph in a 1x3 subgraph layout
plt.subplot(133)

# Show second Gaussian filtered image
plt.imshow(blur2)

# Set the title of the selected subgraph
plt.title("Blur2")

# Show all plots created in Matplotlib
plt.show()

Titles = ["Original","Blur1","Blur2"]
images = [image, blur1, blur2]

count = 3

for i in range(count):
    plt.subplot(1, 3, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
