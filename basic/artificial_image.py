#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:29:37 2023

@author: mehmetakkan
"""

# Imports the OpenCV library for image processing.
import cv2

# Reads an image via the specified file path and loads it in color (BGR).
image = cv2.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg",cv2.IMREAD_COLOR)

# Displays the read image on the screen.
cv2.imshow("image",image)

# Copies the original image.
b = image.copy()

# Resets other color channels, keeping only the blue color channel.
b[:, :, 1] = 0 # The green channel is reset.
b[:, :, 2] = 0 # The red channel is reset.

# Creates a copy of the original image.
g = image.copy()

# Resets other color channels, keeping only the green color channel.
g[:, :, 0] = 0 # The blue channel is reset.
g[:, :, 2] = 0 # Kırmızı kanal sıfırlanır.

# Creates a copy of the original image.
r = image.copy()
# Resets other color channels, keeping only the red color channel.
r[:, :, 0] = 0 # The blue channel is reset.
r[:, :, 1] = 0 # The green channel is reset.

# Displays copied images with different color channels separately on the screen.
cv2.imshow("B-RGB", b) # Shows the image containing only the color blue.
cv2.imshow("G-RGB", g) # Shows the image containing only the green color.
cv2.imshow("R-RGB", r) # Shows the image containing only the red color.

# It continues to show images on the screen until the user presses any key.
cv2.waitKey(0)


