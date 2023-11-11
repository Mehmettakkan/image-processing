# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

# Read a color image
img = cv2.imread("/.../.../.../.../image_processing/images/cube.jpg",cv2.IMREAD_COLOR)

# Show the color image in the window named "image"
cv2.imshow("image",img)

# Convert image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show grayscale image in window named "image"
cv2.imshow("image", gray_image)

# Make you wait until you press any key
cv2.waitKey(0)
