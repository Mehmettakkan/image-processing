#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:36:34 2024

@author: mehmetakkan
"""

import cv2  # OpenCV için görüntü işleme
import numpy as np  # NumPy için sayısal işlemler ve dizi manipülasyonu
import matplotlib.pyplot as plt  # Görüntüleri görüntülemek için Matplotlib

# Görüntünün yolu
path = "/Users/mehmetakkan/Desktop/my_work/image_processing/images/shapes_BGR.jpeg"

# Görüntüyü OpenCV ile oku
image = cv2.imread(path) # kenarlar belirsiz ve düzensizdir

# Görüntüyü gri tonlamaya dönüştürün
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Kenar algılama için basitleştirir

# Morfolojik işlemler için 6x6 yapılandırma elemanı (kernel) oluştur
kernel = np.ones((6, 6), np.uint8)

# Parlak bölgeleri (ön plan) genişletmek için genişletmeyi uygular,
img_dilation = cv2.dilate(image, kernel, iterations=1)  # Kenarları güçlendirir, ancak küçük boşluklar ve delikler oluşturur.

# Morfolojik gradyanı hesaplamak için kenarları vurgular
gradient = cv2.morphologyEx(img_dilation, cv2.MORPH_GRADIENT, kernel, iterations=1) # kenarları daha belirgin hale getirir
# Morfolojik gradyan, bir görüntünün genişletilmesi ve erozyonunun farkı olarak hesaplanır.

# Kenarların içindeki küçük delikleri ve boşlukları doldurmak için kapatmayı uygular
closing = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, kernel)

# Görüntüleri görüntülemek için başlıklar ve görüntüler
Titles = ["Orijinal", "Genişleme", "Gradyan", "Kapatma"]
imgs = [image, img_dilation, gradient, closing]

count = len(Titles)
for i in range(count):
    plt.subplot(1, 4, i + 1)  # Görüntüleri 1 satır, 4 sütunda düzenler
    plt.title(Titles[i])  # Her görüntü için başlık ayarlar
    plt.axis('off')  # Daha temiz görselleştirme için eksen etiketlerini kapatır
    plt.imshow(imgs[i], cmap='gray')  # Görüntüleri gri tonlamalı olarak görüntüler
    plt.imshow(imgs[i])
    
# Grafiği göster
plt.show()