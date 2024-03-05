#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:00:07 2024

@author: mehmetakkan
"""

import cv2 # görüntü işleme
import numpy as np # matematiksel işlemler
import matplotlib.pyplot as plt # görselleştirme işlemleri için


# Görüntü gri tonlamalı olarak yüklenir
# Nedeni, gri tonlamalı görüntülerin renk bilgilerini içermemesinin, 
# kenar tespiti gibi işlemleri daha kolay hale getirmesidir.
image = cv2.imread('/Users/mehmetakkan/Desktop/my_work/image_processing/images/parrot.png', cv2.IMREAD_GRAYSCALE)

# Canny Kenar Tespit
canny_edges = cv2.Canny(image, 50, 150) # Alt eşik 50, üst eşik 150

# Prewitt operatörünün x ve y yönlerindeki filtreleri tanımlanmaktadır
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]) #
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Prewitt operatörü kullanılarak görüntünün x ve y yönlerindeki türevleri 
# hesaplanarak kenarların tespiti yapılmaktadır.
prewitt_edges_x = cv2.filter2D(image, -1, kernel_x)
prewitt_edges_y = cv2.filter2D(image, -1, kernel_y)

# x ve y yönlerindeki türevlerin değerlerinin karelerinin toplamı alınmakta ve 
# bu değere kök alınarak kenarların kalınlığı hesaplanarak kenar tespiti yapılmaktadır.
prewitt_magnitude = np.sqrt(prewitt_edges_x**2 + prewitt_edges_y**2)

# Sobel operatörü kullanılarak görüntünün x ve y yönlerindeki türevleri 
# hesaplanarak kenarların tespiti yapılmaktadır.
sobel_edges_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_edges_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# tespit edilen x ve y yönlerindeki türevlerin değerlerinin karelerinin toplamı 
# alınmakta ve bu değere kök alınarak kenarların kalınlığı hesaplanarak kenar tespiti yapılmaktadır.
sobel_magnitude = np.sqrt(sobel_edges_x**2 + sobel_edges_y**2)

# sonuçları görselleştirmek için kullanılacak başlıkları ve görüntüleri içeren listeler.
Titles = ["Orjinal", "Canny", "Prewitt", "Sobel", "Prewitt X Yönü", "Prewitt Y Yönü"]
imgs = [image, canny_edges, prewitt_magnitude, sobel_magnitude, prewitt_edges_x, prewitt_edges_y]

# görüntü sayısına göre subplotlar oluşturulmakta ve görüntüler gösterilecek figürün boyutu ayarla.
count = len(Titles)
plt.figure(figsize=(15, 10))

for i in range(count):
    
    plt.subplot(2, 3, i + 1)
    plt.title(Titles[i])
    plt.axis('off')
    plt.imshow(imgs[i], cmap='gray')

plt.show()