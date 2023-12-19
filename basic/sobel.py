#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:56:43 2023

@author: mehmetakkan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter

# Vertical and horizontal filter matrices are defined
vertical_filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
horizontal_filter = [[-1, 0, 1], [-2, 0, -2], [-1, 0, 1]]

# The image file is read
img = plt.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/cup.png")

# Image dimensions are taken
n, m, d = img.shape

# A copy is created to keep the edge detection result
edges_img = img.copy() #A copy of the original image is created to keep the edge detection result.

# Operation is performed on each pixel with a two-layer loop
#Processing is performed on each pixel with a two-layer loop. 
#Since the edge detection filter is 3x3, a distance of 3 pixels is left 
#for processing as it approaches the edges.
for row in range(3, n-2):
    for col in range(3, m-2):
        
        # A 3x3 area around each pixel is taken
        local_pixels = img[row-1:row+2, col-1:col+2, 0]
        
        # Vertical edge detection filter applied
        vertical_transformed_pixels = vertical_filter * local_pixels
        vertical_score = vertical_transformed_pixels.sum() / 4
        
        # Horizontal edge detection filter applied
        horizontal_transformed_pixels = horizontal_filter * local_pixels
        horizontal_score = vertical_transformed_pixels.sum() / 4
        
        # Edge score per pixel is calculated
        edge_score = (vertical_score**2 + horizontal_score**2)**.5
        
        # Pixel value is changed with edge detection score
        edges_img[row,col] = [edge_score] * 1

# The edge detection result is normalized        
edges_img = edges_img / edges_img.max()

# Images are created as a result of original and edge detection
Titles = ["Original","Edges"]
images = [img, edges_img]


for i in range(2):
    plt.subplot(1, 2, i+1),
    plt.imshow(images[i], "gray"),
    plt.xticks([]),
    plt.yticks()    
plt.show() 
