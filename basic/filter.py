#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:16:09 2023

@author: mehmetakkan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter

# Official file path
image_path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/brain.jpg"

# Open image
image = Image.open(image_path)

# Kernel size for smoothing
kernel_size = 1

# Create the kernel to be used for smoothing
kernel = np.ones((kernel_size, kernel_size), dtype = np.float32)

# Normalize the kernel, which ensures that each pixel is averaged during the filtering process
kernel /= (kernel_size * kernel_size)

# Determine the depth (ddepth) of the output image
ddepth = -1 # Will be the same as the depth of the input image

# Soften the image with the OpenCV filter2D function
dst = cv2.filter2D(np.array(image), ddepth, kernel)

# Create a new figure in Matplotlib
plt.figure(figsize=(15,12))

# First subgraph: Original image
plt.subplot(121)
plt.title("Originial")
plt.imshow(image)

# Second subgraph: Softened image
plt.subplot(122)
plt.title("Blured")
plt.imshow(dst)

# Show entire chart
plt.show()