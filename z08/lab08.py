from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow, ImageFilter
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zad1

obraz = Image.open('obraz.jpg').convert('L')
print(obraz.mode)

# Zad2

obrazStat = stat.Stat(obraz)

print("Ekstrema ", obrazStat.extrema)  # max i min
print("Zlicza ", obrazStat.count)  # zlicza
print("Srednia ", obrazStat.mean)  # srednia
print("Mediana ", obrazStat.median)  # mediana
print("Odchylenie standardowe ", obrazStat.stddev)  # odchylenie standardowe

histogram = obraz.histogram()

plt.figure()
plt.subplot(1, 1, 1)
plt.plot([i for i in range(0, 256)], histogram)
plt.title('Histogram')

# Zad3

def histogram_norm(obraz):
    return np.divide(obraz.histogram(), obraz.size[0] * obraz.size[1])

plt.figure()
plt.subplot(1, 1, 1)
plt.plot([i for i in range(0, 256)], histogram_norm(obraz))
plt.title('Histogram Norm')

# Zad4

def histogram_cumul(obraz):
    h_norm = histogram_norm(obraz)
    h_cum = [h_norm[0]]

    for i in range(1, 256):
        h_cum.append(h_cum[i - 1] + h_norm[i])

    return h_cum

plt.figure()
plt.subplot(1, 1, 1)
plt.plot([i for i in range(0, 256)], histogram_cumul(obraz))
plt.title('Histogram Cumul')

# Zad5

def histogram_equalization(obraz):
    h_cum = histogram_cumul(obraz)
    obrazCoppy = obraz.copy()
    obrazLoad = obrazCoppy.load()

    for i in range(0, obraz.size[0]):
        for j in range(0, obraz.size[1]):
            tmp = obrazLoad[i, j]
            obrazLoad[i, j] = int(255 * h_cum[tmp])
    return obrazCoppy

equalized = histogram_equalization(obraz)
equalized.save('equalized.png')

# Zad 6

equalized1 = ImageOps.equalize(obraz)
equalized1.save('equalized1.png')

#ImageChops.difference(equalized, equalized1).show()

histogram_eq = equalized1.histogram()

plt.figure()
plt.subplot(2, 2, 1)
plt.plot([i for i in range(0, 256)], histogram)
plt.title('Histogram')

plt.subplot(2, 2, 2)
plt.plot([i for i in range(0, 256)], histogram_norm(obraz))
plt.title('Histogram Norm')

plt.subplot(2, 2, 3)
plt.plot([i for i in range(0, 256)], histogram_cumul(obraz))
plt.title('Histogram Cumul')

plt.subplot(2, 2, 4)
plt.plot([i for i in range(0, 256)], histogram_eq)
plt.title('Histogram Equalization')

#plt.show()

obrazStat2 = stat.Stat(equalized)

print("equalized.png")
print("Ekstrema ", obrazStat2.extrema)  # max i min
print("Zlicza ", obrazStat2.count)  # zlicza
print("Srednia ", obrazStat2.mean)  # srednia
print("Mediana ", obrazStat2.median)  # mediana
print("Odchylenie standardowe ", obrazStat2.stddev)  # odchylenie standardowe

obrazStat3 = stat.Stat(equalized1)

print("equalized1.png")
print("Ekstrema ", obrazStat3.extrema)  # max i min
print("Zlicza ", obrazStat3.count)  # zlicza
print("Srednia ", obrazStat3.mean)  # srednia
print("Mediana ", obrazStat3.median)  # mediana
print("Odchylenie standardowe ", obrazStat3.stddev)  # odchylenie standardowe

# Zad 7

plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(obraz.filter(ImageFilter.DETAIL),'gray')
plt.axis('off')
plt.title('DETAIL')

plt.subplot(2, 2, 2)
plt.imshow(obraz.filter(ImageFilter.SHARPEN),'gray')
plt.axis('off')
plt.title('SHARPEN')

plt.subplot(2, 2, 3)
plt.imshow(obraz.filter(ImageFilter.CONTOUR),'gray')
plt.axis('off')
plt.title('CONTOUR')

plt.subplot(2, 2, 4)
plt.imshow(obraz, 'gray')
plt.axis('off')
plt.title('equalized1.png')

plt.savefig('filtry.png')