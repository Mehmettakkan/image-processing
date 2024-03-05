#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:22:51 2023

@author: mehmetakkan
"""

# Imports the second version of the imageio library with the name 'iio'.
import imageio.v2 as iio

# Loads an image from the specified file path.
image  = iio.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg")

# Displays the size (width, height, color channels) of the image.
print(image.shape)