#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:00:14 2023

@author: mehmetakkan
"""
# Uses the Matplotlib library to import the necessary tools for graphical representation.
import matplotlib.pyplot as plt

# Imports the tools required to load and process image files.
import matplotlib.image as mpimg

# Loads image files from the specified file path.
img1 = mpimg.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/mains.jpg") 
img2 = mpimg.imread("/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg")


# Two different figures are created. There are subplots within each one.
# The first figure is created
plt.figure(1)

# A subplot is created within the created figure and the first image is shown in this region.
plt.subplot(121)
plt.imshow(img1)

plt.figure(1)
# A second subplot is created within the created figure and the second image is shown in this region.
plt.subplot(122)
plt.imshow(img2)

#Those who get an Important error when it runs should type %matplotlib auto 
#into the console.

# A new figure is created.
plt.figure(2)

# A sub-region is created within the newly created figure and the first image is displayed in this region.
plt.subplot(211)
plt.imshow(img1)

plt.figure(2)
# A second sub-region is created within the new figure created and the second image is displayed in this region.
plt.subplot(212)
plt.imshow(img2)



