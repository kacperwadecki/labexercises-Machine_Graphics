from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt


# Zad1

im1 = Image.open('obraz.jpg')
print("Rozmiar obrazu: ", im1.size)
print("Format obrazu: ", im1.format)
print("Tryb obrazu: ", im1.mode)
#im1.show();

# Zad2
# a

# tablica obrazu
T = np.array(im1)
#tablica kanału r
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r) # obraz w odcieniuach szarości kanału r
print("tryb", im_r.mode)
#tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g) # obraz w odcieniuach szarości kanału g
print("tryb", im_g.mode)
#tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b) # obraz w odcieniuach szarości kanału b
print("tryb", im_b.mode)

# b

im2 = Image.merge('RGB', (im_r, im_g, im_b))
diff_im = ImageChops.difference(im1,im2)

#diff_im.show()

# c

r, g, b = im1.split()  # powstają obrazy

# zapis kanałów do tablic
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)

# porównanie tablic
print("--------porównanie tablic--------------")
porownanie = r_T == t_r
czy_rowne = porownanie.all()
print(czy_rowne)
print("----------------------")

# Zad3

r, g, b = im1.split()  # powstają obrazy

# mieszanie kanałow
im3 = Image.merge('RGB', (r, b, g))
#im3.show()

# a

im3.save("im3.jpg")
im3.save("im3.png")

# b

#Image.open("im3.jpg").show()
#Image.open("im3.png").show()

diff_im2 = ImageChops.difference(Image.open("im3.jpg"), Image.open("im3.png"))
#diff_im2.show()

# c

im1_1jpg = Image.open("obraz1_1.jpg")
im1_1png = Image.open("obraz1_1.png")
im1_1Njpg = Image.open("obraz1_1N.jpg")
im1_1Npng = Image.open("obraz1_1N.png")
im1_2jpg = Image.open("obraz1_2.jpg")
im1_2png = Image.open("obraz1_2.png")
im1_2Njpg = Image.open("obraz1_2N.jpg")
im1_2Npng = Image.open("obraz1_2N.png")



plt.figure(figsize=(32, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(ImageChops.difference(im1_1jpg, im1_1png), "gray")
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(ImageChops.difference(im1_1Njpg, im1_1Npng), "gray")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(ImageChops.difference(im1_2jpg, im1_2png), "gray")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(ImageChops.difference(im1_2Njpg, im1_2Npng), "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
#plt.show()

# Zad4

# zapis kanałów do tablic
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)

w1 = 0.3
w2 = 0.8
w3 = 0.2
szary = w1 * r_T + w2 * g_T + w3 * b_T
im4 = Image.fromarray(szary)
#im4.show()

# a
t = (4500, 4500)
A = np.zeros(t, dtype=np.uint8)
A_im = Image.fromarray(A)

im4_1 = Image.merge('RGB', (A_im, g, b))
#im4_1.show()
im4_2 = Image.merge('RGB', (r, A_im, b))
#im4_2.show()
im4_3 = Image.merge('RGB', (r, g, A_im))
#im4_3.show()

# b

plt.figure(figsize=(32, 16))
plt.subplot(1,3,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im4_1, "gray")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(im4_2, "gray")
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(im4_3, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
#plt.show()

# zad5

ksztalt1 = Image.open("img1.png")
ksztalt2 = Image.open("img2.png")
ksztalt3 = Image.open("img3.png")

r1, g1, b1 = ksztalt1.split()
r2, g2, b2 = ksztalt2.split()
r3, g3, b3 = ksztalt3.split()

img1 = Image.merge('RGB', (r1, g2, b3))
img2 = Image.merge('RGB', (r2, g3, b1))
img3 = Image.merge('RGB', (r3, g1, b2))
img4 = Image.merge('RGB', (r1, g3, b2))
img5 = Image.merge('RGB', (r2, g1, b3))
img6 = Image.merge('RGB', (r3, g2, b1))

plt.figure(figsize=(8, 8))
plt.subplot(2, 3, 1)
plt.imshow(img1)
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(img2)
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(img3)
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(img4)
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(img5)
plt.axis('off')
plt.subplot(2, 3, 6)
plt.imshow(img6)
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')