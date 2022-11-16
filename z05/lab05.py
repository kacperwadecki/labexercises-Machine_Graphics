from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('obraz.jpg')
print("tryb obrazu", obraz.mode)
print("rozmiar", obraz.size)
#obraz.show()

inicjaly = Image.open('inicjaly.bmp')
print('tryb obrazu', inicjaly.mode)
print('rozmiar', inicjaly.size)

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    for i in range(0, inicjaly.size[0]):
        for j in range(0, inicjaly.size[1]):
            if m + i < obraz.size[0] and n + j < obraz.size[1]:
                if inicjaly.getpixel((i, j)) == 0:
                    obraz.putpixel((m + i, n + j), kolor)
            else:
                if inicjaly.getpixel((i, j)) == 0:
                    obraz.putpixel((m + i - obraz.size[0], (n + j) - obraz.size[1]), kolor)

obraz1 = obraz.copy()
wstaw_inicjaly(obraz1, inicjaly, 620, 670, 70)
obraz1.save('obraz1.jpg')
#obraz1.show()

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    for i in range(0, inicjaly.size[0]):
        for j in range(0, inicjaly.size[1]):
            if inicjaly.getpixel((i, j)) == 0:
                if m + i < obraz.size[0] and n + j < obraz.size[1]:
                    pixel = obraz.getpixel((i + m, j + n))
                    obraz.putpixel((i + m, j + n), (pixel[0] + x, pixel[1] + y, pixel[2] + z))
                else:
                    pixel = obraz.getpixel((i + (m - obraz.size[0]), j + (n - obraz.size[1])))
                    obraz.putpixel((i + (m - obraz.size[0]), j + (n - obraz.size[1])), (pixel[0] + x, pixel[1] + y, pixel[2] +z))

obraz2 = obraz.copy()
wstaw_inicjaly_maska(obraz2, inicjaly, 310, 335, 100, 100, 100)
obraz2.save('obraz2.jpg')
#obraz2.show()

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obrazL = obraz.load()
    inicjalyL = inicjaly.load()
    for i in range(0, inicjaly.size[0]):
        for j in range(0, inicjaly.size[1]):
            if m + i < obraz.size[0] and n + j < obraz.size[1]:
                if inicjalyL[i, j] == 0:
                    obrazL[m + i, n + j] = kolor
            else:
                if inicjalyL[i, j] == 0:
                    obrazL[m + i - obraz.size[0], (n + j) - obraz.size[1]] = kolor

obraz3 = obraz.copy()
wstaw_inicjaly_load(obraz3, inicjaly, 620, 670, 70)
#obraz3.show()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    obrazL = obraz.load()
    inicjalyL = inicjaly.load()
    for i in range(0, inicjaly.size[0]):
        for j in range(0, inicjaly.size[1]):
            if inicjalyL[i, j] == 0:
                if m + i < obraz.size[0] and n + j < obraz.size[1]:
                    pixel = obrazL[i + m, j + n]
                    obrazL[i + m, j + n] = (pixel[0] + x, pixel[1] + y, pixel[2] + z)
                else:
                    pixel = obrazL[(i + (m - obraz.size[0]), j + (n - obraz.size[1]))]
                    obrazL[i + (m - obraz.size[0]), j + (n - obraz.size[1])] = (pixel[0] + x, pixel[1] + y, pixel[2] + z)

obraz4 = obraz.copy()
wstaw_inicjaly_maska_load(obraz4, inicjaly, 310, 335, 100, 100, 100)
#obraz4.show()

def kontrast(obraz, wsp_kontrastu):
    if wsp_kontrastu >= 0 and wsp_kontrastu <= 100:
        mn = ((255 + wsp_kontrastu) / 255) ** 2
        return obraz.point(lambda i: 128 + (i - 128) * mn)

def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))

def transformacja_gamma(obraz, gamma):
    if gamma > 0:
        return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)

img4 = Image.open('Ananas.jpg')
img5 = img4.copy()
#kontrast(img5, 10).show()
#kontrast(img5, 50).show()
#kontrast(img5, 90).show()

img6 = img4.copy()
#transformacja_logarytmiczna(img6).show()

img7 = img4.copy()
#transformacja_gamma(img7, 1).show()
#transformacja_gamma(img7, 5).show()
#transformacja_gamma(img7, 10).show()

def zad5(obraz, wartosc):
    tmp = np.array(obraz, dtype='uint8')
    for i in range(0, obraz.size[1]):
        for j in range(0, obraz.size[0]):
            p = tmp[i, j]
            if p[0] + wartosc > 255:
                p[0] = 255
            else:
                p[0] = p[0] + wartosc
            if p[1] + wartosc > 255:
                p[1] = 255
            else:
                p[1] = p[1] + wartosc
            if p[2] + wartosc > 255:
                p[2] = 255
            else:
                p[2] = p[2] + wartosc
            tmp[i, j] = (p[0], p[1], p[2])
    return Image.fromarray(tmp, "RGB")

im = Image.open('obraz.jpg')
im1 = im.copy()
im2 = im.copy()
im3 = im.copy()


T = np.array(im1, dtype='uint8')
T += 100
obraz_wynik = Image.fromarray(T, 'RGB')
obraz_wynik.show()

im2.point(lambda i: i + 100).show()

zad5(im3, 100).show()


