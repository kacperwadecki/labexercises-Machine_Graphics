from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageEnhance
from PIL import ImageStat as stat

# Zadanie 1

image = Image.open('obraz.png')
imageCopy = image.copy()
#print(image.size, image.mode)

# a

w, h = image.size
s_w = 0.15
s_h = 0.27
resample_method =['NEAREST','LANCZOS','BILINEAR','BICUBIC','BOX','HAMMING']
im_N = image.resize((int(w*s_w), int(h*s_h)), 0)
plt.figure(figsize=(16, 12))
i=1

for t in range(6):
    file_name = "resample_"+ str(resample_method[t])
    im_r = image.resize((int(w*s_w), int(h*s_h)), t)
    plt.subplot(6, 2, i)
    plt.title(str(file_name))
    plt.imshow(im_r)
    plt.axis('off')
    i +=1
    diff=ImageChops.difference(im_N,im_r)
    s = stat.Stat(diff)
    plt.subplot(6, 2, i)
    plt.title('srednia' + str(np.round(s.mean, 2)))
    plt.imshow(diff)
    plt.axis('off')
    i +=1

# b

s_wb = 1/0.15
s_hb = 1/0.27
i=1
plt.figure(figsize=(16, 12))

for t in range(6):
    im_r = imageCopy.resize((int(w * s_w), int(h * s_h)), t)
    w2, h2 = im_r.size
    file_name = "resample_" + str(resample_method[t])
    im_rb = im_r.resize((int(w2 * s_wb), int(h2 * s_hb)), t)
    #print(im_rb.size)
    plt.subplot(6, 1, i)
    plt.title(str(file_name))
    plt.imshow(im_rb)
    plt.axis('off')
    i += 1

# Zadanie 2

w_p = 200
h_p=30
w_k=700
h_k=470
wycinek = (w_p, h_p, w_k, h_k) # definicja miejsca wycięcia w_p, h_p - lewy górny róg, w_k,h_k prawy dolny róg
wyc_w = wycinek[2] - wycinek[0] # szerokość wycinka
wyc_h = wycinek[3] - wycinek[1] # wysokość wycinka
s_w = 2 # skala dla szerokości
s_h = 3 # skala dla wysokości

glowa = image.resize((s_w * wyc_w, s_h * wyc_h) , box = wycinek)# wycina wycienek i zmienia rozmiar wycinka
glowa1 = image.crop(wycinek)
glowa1 = glowa1.resize((s_w * wyc_w, s_h * wyc_h))

plt.figure(figsize=(16, 12))
plt.subplot(3, 1, 1)
plt.title("glowa")
plt.imshow(glowa)
plt.axis('off')

plt.subplot(3, 1, 2)
plt.title("glowa1")
plt.imshow(glowa1)
plt.axis('off')

plt.subplot(3, 1, 3)
plt.title("diff")
plt.imshow(ImageChops.difference(glowa,glowa1))
plt.axis('off')

print("glowa", glowa.size)
print("glowa1", glowa1.size)

# Zadanie 3

rot_60_exp_fill = image.rotate(60, expand=1, fillcolor=(255,0,0))
rot_60_fill = image.rotate(60, fillcolor=(255,0,0))
rot_300_exp_fill = image.rotate(300, expand=1, fillcolor=(0,0,255))
rot_300_fill = image.rotate(300, fillcolor=(0,0,255))

plt.figure(figsize=(16, 12))
plt.subplot(4, 1, 1)
plt.title("rot60_exp_fill")
plt.imshow(rot_60_exp_fill)
plt.axis('off')

plt.subplot(4, 1, 2)
plt.title("rot_60_fill")
plt.imshow(rot_60_fill)
plt.axis('off')

plt.subplot(4, 1, 3)
plt.title("rot_300_exp_fill")
plt.imshow(rot_300_exp_fill)
plt.axis('off')

plt.subplot(4, 1, 4)
plt.title("rot_300_fill")
plt.imshow(rot_300_fill)
plt.axis('off')

# Zadanie 4

black = Image.fromarray(np.zeros((1760, 1874, 3), np.uint8))
black2 = Image.fromarray(np.zeros((3520, 3748, 3), np.uint8))

black.paste(image, (0, 0))
black2.paste(black, (1960, 1674))
black2 = black2.rotate(30)
black2.save("obrot.png")

# Zadanie 5

obraz3 = Image.open("balwan.png")

t1 = obraz3.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
t1 = t1.rotate(90, expand=1)

t2 = obraz3.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
t2 = t2.rotate(270, expand=1)