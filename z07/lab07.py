from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt

# Zadanie 1
obraz = Image.open('obraz.jpg')

def filtruj(obraz, kernel, scale):
    w, h = obraz.size
    kernelLen = len(kernel)
    obrazCopy = obraz.copy()
    obrazCopyTable = obrazCopy.load()
    obrazTable = obraz.load()

    for i in range(int(kernelLen / 2), w - int(kernelLen / 2)):
        for j in range(int(kernelLen / 2), h - int(kernelLen / 2)):
            tmp = [0, 0, 0]
            for k in range(kernelLen):
                for l in range(kernelLen):
                    x = i + k - int(kernelLen / 2)
                    y = j + l - int(kernelLen / 2)
                    frame = obrazTable[x, y]
                    for m in range(3):
                        tmp[m] += frame[m] * kernel[k][l]

            obrazCopyTable[i, j] = (int(tmp[0] / scale), int(tmp[1] / scale), int(tmp[2] / scale))
    return obrazCopy


#filtruj(obraz, [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],1).show()
#obraz.show()

# Zadanie 2

#print(ImageFilter.BLUR.filterargs)

blur = filtruj(obraz, [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]],16)

blur1 = obraz.filter(ImageFilter.BLUR)

blurDiff = ImageChops.difference(blur, blur1)

plt.subplot(3, 1, 1)
plt.imshow(blur)
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(blur1)
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(blurDiff)
plt.axis('off')
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig('fig1.png')

# Zadanie 3

print(ImageFilter.EMBOSS.filterargs)

obrazL = obraz.convert('L')

ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1,  0,  1, -2,  0,  2, -1,  0,  1))
sobel1 = obrazL.filter(ImageFilter.EMBOSS)
#sobel1.show()

ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0,  0, 0, 1, 2, 1))
sobel2 = obrazL.filter(ImageFilter.EMBOSS)
#sobel2.show()

plt.subplot(3, 1, 1)
plt.imshow(obrazL)
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(sobel1)
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(sobel2)
plt.axis('off')
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig('fig2.png')

# Zadanie 4

plt.figure(facecolor='white')
plt.subplot(4, 2, 1)
plt.imshow(obraz.filter(ImageFilter.DETAIL()))
plt.title("DETAIL")
plt.axis('off')
plt.subplot(4, 2, 2)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.DETAIL())))
plt.title("Różnica")
plt.axis('off')
plt.subplot(4, 2, 3)
plt.imshow(obraz.filter(ImageFilter.EDGE_ENHANCE_MORE()))
plt.title("EDGE_ENHANCE_MORE")
plt.axis('off')
plt.subplot(4, 2, 4)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.EDGE_ENHANCE_MORE())))
plt.title("Różnica")
plt.axis('off')
plt.subplot(4, 2, 5)
plt.imshow(obraz.filter(ImageFilter.SHARPEN()))
plt.title("SHARPEN")
plt.axis('off')
plt.subplot(4, 2, 6)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.SHARPEN())))
plt.title("Różnica")
plt.axis('off')
plt.subplot(4, 2, 7)
plt.imshow(obraz.filter(ImageFilter.SMOOTH_MORE()))
plt.title("SMOOTH_MORE")
plt.axis('off')
plt.subplot(4, 2, 8)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.SMOOTH_MORE())))
plt.title("Różnica")
plt.axis('off')
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig('fig3.png')

# b

plt.figure(facecolor='white')
plt.subplot(5, 2, 1)
plt.imshow(obraz.filter(ImageFilter.GaussianBlur(radius=5)))
plt.title("GaussianBlur radius=5",fontsize=7)
plt.axis('off')
plt.subplot(5, 2, 2)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.GaussianBlur(radius=5))))
plt.title("różnica",fontsize=7)
plt.axis('off')

plt.subplot(5, 2, 3)
plt.imshow(obraz.filter(ImageFilter.UnsharpMask(radius=5, percent=250, threshold=3)))
plt.title("UnsharpMask radius=5, percent=250, threshold=3",fontsize=7)
plt.axis('off')
plt.subplot(5, 2, 4)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.UnsharpMask(radius=5, percent=250, threshold=3))))
plt.title("różnica",fontsize=7)
plt.axis('off')

plt.subplot(5, 2, 5)
plt.imshow(obraz.filter(ImageFilter.MedianFilter(size=3)))
plt.title("MedianFilter size=3",fontsize=7)
plt.axis('off')
plt.subplot(5, 2, 6)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.MedianFilter(size=3))))
plt.title("różnica",fontsize=7)
plt.axis('off')

plt.subplot(5, 2, 7)
plt.imshow(obraz.filter(ImageFilter.MinFilter(size=5)))
plt.title("MinFilter size=5",fontsize=7)
plt.axis('off')
plt.subplot(5, 2, 8)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.MinFilter(size=5))))
plt.title("różnica",fontsize=7)
plt.axis('off')

plt.subplot(5, 2, 9)
plt.imshow(obraz.filter(ImageFilter.MaxFilter(size=5)))
plt.title("MaxFilter size=5",fontsize=7)
plt.axis('off')
plt.subplot(5, 2, 10)
plt.imshow(ImageChops.difference(obraz, obraz.filter(ImageFilter.MaxFilter(size=5))))
plt.title("różnica",fontsize=7)
plt.axis('off')
plt.savefig('fig4.png')