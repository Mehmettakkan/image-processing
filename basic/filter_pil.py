#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:35:43 2024

@author: mehmetakkan
"""

import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

image = Image.open("/Users/mehmetakkan/Desktop/my_work/image_processing/images/mains.jpg")

# Convert image to grayscale
image = image.convert("L")

# Apply edge detection filter to the image
image = image.filter(ImageFilter.FIND_EDGES)

# Visualize the image with matplotlib library
plt.imshow(image, cmap="gray")


# Bu noktada görüntü ekrana çizilmiş olacak, ancak ekranda göstermek için
plt.show() #fonksiyonunu kullanmak daha iyi bir uygulama olabilir.