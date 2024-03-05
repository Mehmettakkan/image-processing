#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sun Jan 14 12:12:11 2024 tarihinde oluşturuldu

@author: mehmetakkan  # Yazar bilgileri
"""

import cv2       # Görüntü işleme için OpenCV kütüphanesini içeriyor
import matplotlib.pyplot as plt  # Görüntüleri görüntülemek için Matplotlib kütüphanesini içeriyor

# Belirtilen yoldan görüntüyü okur
image = cv2.imread('/Users/mehmetakkan/Desktop/my_work/image_processing/images/simple.jpg')

# Morfolojik işlemler için eliptik bir yapı elemanı oluşturur
elliptical_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Küçük nesneleri kaldırmak ve kenarları yumuşatmak için genişletme uygulanır
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, elliptical_kernel, iterations=2)

# İkilik görüntüye dönüştürmek için bir eşik değeri ayarla
threshold = 128

# genişletme uygulanan görüntüyü eşiğe göre ikilik (siyah beyaz) dönüştürür
binary_image = cv2.threshold(opened_image, threshold, 255, cv2.THRESH_BINARY)[1]

# Parlak bölgeleri daha da küçültmek için erozyon uygular
eroded_image = cv2.erode(binary_image, elliptical_kernel, iterations=2)

# Görüntüleri görüntülemek için başlıklar ve görüntüler hazırlar
Titles1 = ['Orijinal', 'Açma', 'Erozyon']
images1 = [image, opened_image, eroded_image]

# Görüntülerin sayısını sayar
count = len(Titles1)

# Şema boyutunu ayarlamak için yorumu kaldırın
# plt.figure(figsize=(15, 10))

# Her görüntü için bir alt grafik oluşturur ve görüntüler
for i in range(count):
    plt.subplot(1, 3, i+1)  # 1 satır ve 3 sütundan oluşan bir ızgarada bir alt grafik oluşturur
    plt.title(Titles1[i])  # Alt grafik için başlık ayarlar
    plt.axis('off')  # Temiz bir görüntü için eksenleri kapat
    plt.imshow(images1[i])  # Alt grafikte görüntüyü görüntüle

plt.show()  # Tüm görüntüleri içeren son çizimi göster