#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:14:28 2024

@author: mehmetakkan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg"

#orijinal görüntü
image = cv2.imread(path, cv2.IMREAD_COLOR)

#görüntüyü BGR formatından RGB formatına dönüştürür.
original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#Görüntü kopyalandı
blue_image = original_image.copy();

#Mavi bantı oluşturmak için yeşil kanalı sıfırladım
blue_image[:, :, 1] = 0

#Mavi bantı oluşturmak için kırmızı kanalı sıfırladım
blue_image[:, :, 2] = 0



#Görüntü kopyalandı
green_image = original_image.copy();

#yeşil bandı oluşturmak için mavi kanal sıfırlandı
green_image[:, :, 0] = 0

#yeşil bandı oluşturmak için kırmızı kanal sınırlandı
green_image[:, :, 2] = 0



#Görüntü kopyalandı
red_image = original_image.copy();

#kırmızı bantı oluşturmak için mavi kanalı sıfırladım
red_image[:, :, 0] = 0

#kırmızı bantı oluşturmak için yeşil bantı sıfırladım
red_image[:, :, 1] = 0


Titles = ["Original", "Mavi", "Yeşil", "Kırmızı"]
images = [original_image, blue_image, green_image, red_image]

count = 4

for i in range(count):
    plt.subplot(2, 2, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
    

# Yapay görüntü
height, width = original_image.shape[:2]

artificial_image = np.zeros((height, width, 3), dtype=np.uint8)

artificial_image[:, :, 0] = 255  # Mavi bandı
artificial_image[:, :, 1] = 108  # Yeşil bandı
artificial_image[:, :, 2] = 0    # Kırmızı bandı

# Oluşturulan yapay görüntüyü görselleştir
plt.imshow(artificial_image)
plt.title('Artificial Image')
plt.show()