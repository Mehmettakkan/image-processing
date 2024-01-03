#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:00:51 2024

@author: mehmetakkan
"""
#example for threshold 3 band
import cv2
import matplotlib.pyplot as plt

path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/mains.jpg"

# Read image in BGR format
image = cv2.imread(path, cv2.IMREAD_COLOR)

# Convert image to grayscale
#Grayscale conversion is often used to simplify image analysis tasks that do not require color information.
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# This applies a thresholding filter to the grayscale image. 
#It only keeps pixels with intensity values between 190 and 255 inclusive, 
#effectively creating a black and white mask that highlights brighter areas.
gray_filtered = cv2.inRange(gray, 190, 255)

RGB = cv2.imread(path)

#This applies thresholding in the RGB color space, keeping only pixels with 
#values between (190, 190, 190) and (255, 255, 255) in all three color channels. 
#This creates a mask that highlights bright areas in the original color image.
RGB_filtered = cv2.inRange(RGB, (190, 190, 190), (255, 255, 255))


#This creates a shape for drawing images.
plt.figure(figsize=(15, 12))

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.subplot(131)
plt.imshow(image)
plt.title("original")

plt.subplot(132)
plt.imshow(gray_filtered, "gray")
plt.title("gray")

plt.subplot(133)
plt.imshow(RGB_filtered)
plt.title("rgb")

Titles = ["original", "gray", "rgb"]
imgs = [image, gray_filtered, RGB_filtered]

# count = 3
    
# for i in range(count):
#     plt.subplot(1, 3, i+1)
#     plt.title(Titles[i])
#     plt.imshow(imgs[i])
# plt.show()


#Bir görüntü aldığımızda, bu görüntüye uygulayacak olduğumuz threshold değerlerini değiştirerek
#bölütlemesini bulmak istediğim kenar bilgilerine göre threshold değerlerini değiştirmek gerekecek.
