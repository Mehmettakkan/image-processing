#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:09:07 2024

@author: mehmetakkan
"""

import cv2
import matplotlib.pyplot as plt


#3 farklı resmi dosya yolu belirtildi
path_1 = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/cube.jpg"

path_2 = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/penguin.jpg"

path_3 = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/potatoes.jpg"

#3 farklı resim okunuldu
image_1 = cv2.imread(path_1)
#gri resim
image_2 = cv2.imread(path_2)
#gri resim
image_3 = cv2.imread(path_3)


#Okunan tüm görüntüleri BRG formatından RGB formatına dönüştürdüm
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)
image_3 = cv2.cvtColor(image_3, cv2.COLOR_BGR2RGB)



#Threshol degerleri belirle
thresh = 120

# Belirtilen eşiğin üzerindeki pikselleri beyaza (255) ve altındaki pikselleri siyaha (0) ayarlar.
ret, thresh1 = cv2.threshold(image_1 , thresh, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image_2 , thresh, 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(image_3 , thresh, 255, cv2.THRESH_BINARY)

# Başlıkları ve görselleri içeren listeler oluşturulur.
Titles = ["Image_1", "Image_1_THRESH","Image_2","Image_2_THRESH","Image_3","Image_3_THRESH"]
images = [image_1, thresh1, image_2, thresh2, image_3, thresh3]

#Toplam resim sayısı
count = 6

# Matplotlib kullanarak görüntüleri ekranda görüntüler.
for i in range(count):
    plt.subplot(3, 2, i+1) # 3x2'lik bir alt grafik oluşturur ve her görüntüyü yerleştirir.
    plt.title(Titles[i]) #başlıkları gez ve yaz
    plt.imshow(images[i]) #resimleri gez ve ekrana yazdır
plt.show() 