#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:38:03 2023

@author: mehmetakkan
"""

import matplotlib as plt
# Imports the OpenCV library for image processing.
import cv2
# Imports the NumPy library for array operations and mathematical operations.
import numpy as np

# File path of the image to be processed.
path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg"

# Loads the image from the specified file path.
image = cv2.imread(path)

# Prints the dimensions (height, width, number of channels) of the loaded image on the screen.
print(image.shape) 

# Prints the data type of the loaded image (e.g. uint8) to the screen.
print(image.dtype)

# Prints the total pixel count of the loaded image on the screen.
print(image.size)

# Gets the BGR (Blue, Green, Red) values of the pixel at position (100,100).
px = image[100,100]

# Prints the BGR values of this pixel to the screen.
print(px)

# Assigns new BGR values to a specific pixel.
image[100,100] = 255,0,64

# Prints the blue (channel 0) value of a specific pixel to the screen.
print(image.item(100,100,0))

# Separates the BGR channels of the image separately.
blue, green, red, = cv2.split(image)

# Shows reserved channels on the screen.
# cv2.imshow("Blue", blue)
# cv2.imshow("Green", green)
# cv2.imshow("Red", red)

# Creates a new image by combining green, red and blue channels.
merged = cv2.merge([green, red, blue])

# Displays the newly created image on the screen.
cv2.imshow("merged", merged)

# Creates another image by combining red, blue and green channels.
merged2 = cv2.merge([red, blue, green])

# Shows the other new image created on the screen.
cv2.imshow("merged2", merged2)

cv2.waitKey(0)
#cv2.destroyAllWindows()
