#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:56:43 2023

@author: mehmetakkan
"""
# Import necessary libraries
import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy for numerical operations and array manipulation
import matplotlib.pyplot as plt  # Import Matplotlib for plotting images

# Define vertical and horizontal edge detection filters (highlighting sharp intensity changes)
vertical_filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
horizontal_filter = [[-1, 0, 1], [-2, 0, -2], [-1, 0, 1]]

# Read the image using Matplotlib
img = plt.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/cup.png")

# Get image dimensions (height, width, and color channels)
n, m, d = img.shape

# Create a copy of the original image to store edge detection results
edges_img = img.copy()

# Process each pixel using a double loop, handling edges (leaving a 3-pixel border)
for row in range(3, n-2):  # Iterate over rows, skipping the first and last 3 rows
  for col in range(3, m-2):  # Iterate over columns, skipping the first and last 3 columns

    # Get a 3x3 area around the current pixel for applying filters
    local_pixels = img[row-1:row+2, col-1:col+2, 0]  # Focus on the first color channel

    # Apply vertical and horizontal filters to detect edges in both directions
    vertical_score = np.sum(vertical_filter * local_pixels) / 4  # Calculate vertical edge strength
    horizontal_score = np.sum(horizontal_filter * local_pixels) / 4  # Calculate horizontal edge strength

    # Calculate overall edge score using the Pythagorean theorem
    edge_score = (vertical_score**2 + horizontal_score**2)**0.5

    # Update the pixel value in the edges_img with the calculated edge score
    edges_img[row, col] = [edge_score] * 1  # Assign the edge score to all color channels

# Normalize edge detection results to a range of 0 to 1 for better visualization
edges_img = edges_img / edges_img.max()

# Display both the original and edge-detected images side-by-side
Titles = ["Original", "Edges"]
images = [img, edges_img]
for i in range(2):
  plt.subplot(1, 2, i+1)  # Create subplots for each image
  plt.imshow(images[i], "gray")  # Display in grayscale
  plt.xticks([]), plt.yticks([])  # Hide axis ticks for cleaner visualization
plt.show()  # Show the entire plot