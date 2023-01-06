from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# Zad 1

obraz = Image.open("obraz1.png")
r, g, b, a = obraz.split()
obraz2 = obraz.convert("RGB")

obraz3 = Image.new('RGB', obraz.size, (255, 255, 255))
obraz3.paste(obraz, (0, 0), a)
obraz3.save('obraz3.png')

#obrazDiff = ImageChops.difference(obraz2, obraz3).show()

# Zad 2

obrazCmyk = obraz3.convert('CMYK')
obrazYCbCr = obraz3.convert('YCbCr')
obrazHSV = obraz3.convert('HSV')

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(obrazCmyk, 'gray')
plt.title('CMYK')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(obrazYCbCr, 'gray')
plt.title('YCbCr')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(obrazHSV, 'gray')
plt.title('HSV')
plt.axis('off')
plt.savefig('fig1.png')

r1, g1, b1, a1 = obrazCmyk.split()
r2, g2, b2 = obrazYCbCr.split()
r3, g3, b3 = obrazHSV.split()

plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(r1)
plt.title('CMYK R')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(g1)
plt.title('CMYK G')
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(b1)
plt.title('CMYK B')
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(a1)
plt.title('CMYK A')
plt.axis('off')
plt.savefig('cmyk.png')

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(r2)
plt.title('YCbCr R')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(g2)
plt.title('YCbCr G')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(b2)
plt.title('YCbCr B')
plt.axis('off')
plt.savefig('ycbcr.png')

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(r3)
plt.title('HSV R')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(g3)
plt.title('HSV G')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(b3)
plt.title('HSV B')
plt.axis('off')
plt.savefig('hsv.png')

# Zad 3
obraz4 = Image.open('obraz4.jpg')
obraz4 = obraz4.resize(obraz.size, 1)

obraz4_1 = obraz4.copy()
obraz4_1.paste(obraz, (0,0), a)

obraz4_2 = obraz.copy()
obraz4_2.paste(obraz4, (0, 0), a)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(obraz4_1)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(obraz4_2)
plt.axis('off')
plt.savefig('fig2.png')