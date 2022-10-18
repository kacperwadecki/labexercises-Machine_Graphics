from PIL import Image  # Python Imaging Library
import numpy as np

# ---------- wczytywanie obrazu zapisanego w różnych formatach .bmp, .jpg, .png oraz pobieranie informacji o obrazie  -------------------
obrazek = Image.open("lab1/obrazek.bmp")  # wczytywanie obrazu
obrazek.show()
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

# ---------- wczytywanie obrazu do tablicy oraz pobieranie informacji o tablicach ------------------------------
dane_obrazka = np.asarray(obrazek)
print("---------------- informqcje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementow:", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)  # pokazuje ile współrzednych trzeba do opisania wyrazu tablicy (piksela)
print("pierwszy wyraz:", dane_obrazka[0][0])
print("drugi wyraz:", dane_obrazka[1][0])
print("***************************************")
print(dane_obrazka)  # mozna odkomentować, zeby zobaczyć tablicę

# ------------------------   wczytywanie obrazu do tablicy z jednoczesnym okresleniem typu danych ---------------------
dane_obrazka1 = dane_obrazka * 1  # zmienia typ bool na int
print(dane_obrazka1)
ob_d = Image.fromarray(dane_obrazka)  # tworzenie obrazu z tablicy dane_obrazka (typ bool)
# ----- wyswietlanie informacji o obrazie -----------------------------
print("-------informacje o obrazie ob_d ------------")
print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)
ob_d.show()

print("-------informacje o obrazie ob_d1 ------------")
ob_d1 = Image.fromarray(dane_obrazka1)  # tworzenie obrazu z tablicy dane_obrazka1 (typ int)
# ----- wyswietlanie informacji o obrazie -----------------------------
print("tryb:", ob_d1.mode)
print("format:", ob_d1.format)
print("rozmiar:", ob_d1.size)
ob_d1.show()
# WAŻNE PYTANIE NA NASTEPNE ZAJECIA!!!  DLACZEGO ob_d1 widać jako obraz czarny?


# ---------------- zapisywanie obrazu do pliku -----------------
ob_d.save(
    "lab1/obraz_zapisany.bmp")  # jako argument podajemy nazwę pliku wraz z rozszerzeniem, bo w zależności od tego w jakim formacie zapiszemy otrzymamy różne tablice obrazu

print("-------------------------------------------")

# wczytywanie tablicy z pliku UWAGA! plik txt powinien zawierac same zera i jedynki oddzielane spacjami bez dodatkowych znaków jak w pliku dane.txt
t1 = np.loadtxt("lab1/dane.txt", dtype=np.bool_)
t2 = np.loadtxt("lab1/dane.txt", dtype=np.int_)

# w zależnosci od tego, jakie operacje chcemy zrobić na tablicy, wybieramy jedną z powyższych postaci tablicy
print("typ danych tablicy t1:", t1.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t1 :", t1.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t1 :", t1.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

print("typ danych tablicy t2:", t2.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t2 :", t2.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t2 :", t2.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

print("---- porównywanie tablic ------")
nowa_t1 = np.loadtxt("lab1/dane1.txt", dtype=np.bool_)  # wczytanie tablicy z pliku dane1.txt
nowa_t1_1 = nowa_t1 * 1  # zamiana bool na tablice zero-jedynkową
print("----- nowa_t1 ---------")
print(nowa_t1)
print("------ nowa_t1_1 --------")
print(nowa_t1_1)
porownanie = nowa_t1 == nowa_t1_1  # zwraca TRUE jesli tablice są identyczne (przy czym True = 1, False = 0), w przeciwnym przypadku False
czy_rowne = porownanie.all()
print("czy tablice sa równe? ", czy_rowne)

print("------ drugi przykład -------------------")
nowa_t2 = np.loadtxt("lab1/dane1.txt", dtype=np.int_)  # wczytanie tablicy z pliku dane1.txt
print("--- nowa_t2 -----------")
print(nowa_t2)
print("----- t2 ---------")
print(t2)
porownanie2 = t2 == nowa_t2  # tablica, która ma wartośc True jesli elementy w odpowieednich miejscach sa równe i False w p.p.
print("------ tablica porownanie -------")
print(porownanie2)

# zliczanie ile jest równych elementów
print("wszystkich elementów tablicy t2 jest: ", t2.size)
print("wszystkich elementów tablicy nowa_t2 jest: ", nowa_t2.size)
print("równych elementów jest: ", np.sum(t2 == nowa_t2))  # zlicza ile elementów jest takich samych
print("równych elementów jest: ", np.sum(porownanie2))  # zlicza ile elementów jest takich samych (drugi sposób)

# zapis tablicy do pliku
t2_text = open('lab1/t2.txt', 'w')
for rows in t2:
    for item in rows:
        t2_text.write(str(item) + ' ')
    t2_text.write('\n')
