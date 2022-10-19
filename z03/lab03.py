from PIL import Image  # Python Imaging Library
import numpy as np
import random as rand

def negatyw_szare(tab):  # tworzy tablicę dla negatywu
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg

#zad1
def moje(w, h, dzielnik, m, n, zmiana_koloru):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(w/dzielnik)
    tmp1 = grub

    for i in range(int(h/2)):
        for j in range(int(w/2)):
            tab[i*2, j*2] = (i * zmiana_koloru) % 256

    for i in range(tmp1):
        z1 = h - grub
        z2 = w - grub
        if(i%2 == 0):
            tab[grub:z1, grub:z2] = rand.randint(1, 254)
        else:
            tab[grub:z1, grub:z2] = rand.randint(1, 254)
        grub+=tmp1 - 1

    tab = tab * 255
    obraz = Image.fromarray(tab)  # tworzy obraz
    obraz.show()
    return tab

# moje(480, 320, 8, 100, 50, 10)

# tab_neg = negatyw_szare(moje(480, 320, 8, 100, 50, 10))
# obraz_neg = Image.fromarray(tab_neg)
# obraz_neg.show()

def rysuj_ramke(w, h, dzielnik, kolor, zmiana_koloru):
    t = (h, w)  # rozmiar tablicy
    kolor = zmiana_koloru * kolor % 256
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    tab[:] = kolor
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    tmp1 = grub

    for i in range(tmp1 + 1):
        z1 = h - grub
        z2 = w - grub
        if(i%2 == 0):
            tab[grub:z1, grub:z2] = zmiana_koloru * kolor % 256
        else:
            tab[grub:z1, grub:z2] = zmiana_koloru * kolor % 256
        grub+=tmp1 - 1
        kolor = (zmiana_koloru * kolor) % 256

    return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości

# tab = rysuj_ramke(480, 320, 8, 65, 5)
# im_ramka = Image.fromarray(tab)
# im_ramka.show()
#
# tab_neg = negatyw_szare(tab)
# obraz_neg = Image.fromarray(tab_neg)
# obraz_neg.show()
#
# im_ramka.save("obraz1_1.jpg")
# im_ramka.save("obraz1_1.png")
#
# obraz_neg.save("obraz1_1N.jpg")
# obraz_neg.save("obraz1_1N.png")

# Zad2

def rysuj_pasy_pionowe_kolor(w, h, dzielnik, kolor, zmiana_koloru):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        r = (kolor[0] + k + zmiana_koloru - k * 10) % 256
        g = (kolor[1] + k + zmiana_koloru - k * 10) % 256
        b = (kolor[2] + k + zmiana_koloru - k * 10) % 256
        for m in range(grub):
            i = k * grub + m
            for j in range(h):
                tab[j, i] = [r, g, b]
    return tab

# tab1 = rysuj_pasy_pionowe_kolor(300, 200, 20, [100, 200, 0], 32)
# obraz1 = Image.fromarray(tab1)
# # obraz1.show()
# obraz1.save("obraz2.jpg")
# obraz1.save("obraz2.png")

def negatyw_kolor(tab):  # tworzy tablicę dla negatywu
    h, w, c = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            red = 255 - tab_neg[i][j][0]
            green = 255 - tab_neg[i][j][1]
            blue = 255 - tab_neg[i][j][2]
            tab_neg[i][j] = [red, green, blue]

    return tab_neg

# tab_neg = negatyw_szare(tab1)
# obraz_neg = Image.fromarray(tab_neg)
# obraz_neg.show()
# obraz_neg.save("obraz2N.jpg")
# obraz_neg.save("obraz2N.png")

# Zad3

inicjaly = Image.open("inicjaly.bmp") # wczytywanie obrazu
obraz_wstawiany = np.asarray(inicjaly)

def koloruj(tab_inicjaly, kolor, zmiana_koloru):
    h, w = tab_inicjaly.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if tab_inicjaly[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
        r = (kolor[0] + i * zmiana_koloru) % 256
        g = (kolor[1] + i * zmiana_koloru) % 256
        b = (kolor[2] + i * zmiana_koloru) % 256
        kolor = [r, g, b]
    return tab

obraz2 = Image.fromarray(koloruj(obraz_wstawiany, [120, 240, 50], 100))
obraz2.show()
obraz2.save("obraz3.jpg")
obraz2.save("obraz3.png")