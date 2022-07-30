# MULAKAT-ALISTIRMA SORULARI

# Sicaklik birimlerinden Celsius'u Kelvine ceviren fonksiyonu yaziniz. (kelvin = celcius + 273);
def hesapla(celcius):
    kelvin = celcius + 273
    print(kelvin)

    return kelvin


kelvin = hesapla(30)

kelvin



# Yaş bilgisi argumanli bir fonksiyon yazın, 18 yaş altı için giremezsin, üstü için hoş geldin yazsin;
def yasSiniri(yas):
    if yas < 18:  # False
        print("giremezsin")
    elif yas < 21:  # True
        print("veli ile gir")
    else:
        print("hoş geldin")


yasSiniri(17)





def yasSiniri(yas):
    if yas < 18:  # False
        print("giremezsin")
        return "giremezsin"
    elif yas < 21:  # True
        print("velinle girebilirsin")
    else:
        print("hoş geldin")
        return "hoş geldin"


yasSiniri(19)





# Asagidaki degiskenleri kullanarak dersin matematik olup olmadigini kontrol eden,
# matematik ise "Matematik sinavi aciklandi" ifadesi yazdiran,
# Ders matematikse ayrica puanin 65'ten buyuk olup olmadigini kontrol eden ve
# 65'ten buyuk ise 'Sinavi Gectiniz' ifadesini cikti olarak yazan kodlari yaziniz;

ders = "Matematik"
puan = 70


def dersKontrol(ders, puan):
    if ders == "matematik":
        print("Mat sınavı açıklandı")
        if puan > 65:
            print("geçtin")
        else:
            print("kaldın")
    else:
        print("Mat sınavı açıklanmadı")

dersKontrol(ders, puan)





# Asagida verilen A listesindeki elemanlari for dongusu kullanarak B listesine tasiyiniz;
A = [10, 11, 12, 13, 14, 15, 16]
B = []


def move(liste1, liste2):
    for i in liste1:
        liste2.append(i)

    liste1 = []
    return liste1, liste2


list1, list2 = move(A, B)

list1
list2






# 0'dan 50'ye kadar olan sayilari even ve odd listelerine ekleyiniz;
even = []
odd = []

for i in range(50):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even
odd






# Arguman olarak girilen sayının karesini alan fonksiyonu yaziniz;
def square(n):
    squar = n ** 2

    return squar


square(5)





# Arguman olarak girilen 2 sayının üssünü alan fonksiyonu yaziniz;
def power(a, b):
    powerr = a ** b
    # print(powerr)

    return powerr


pow = power(2, 3)
pow






# Bir sayı listesi alip, bu listenin icindeki tum elemanlari toplayan fonksiyon;
sampleList = [33, 22, 45, 66, 53, 124]


def sumUp(x):
    sum_ = 0
    for i in x:  # 33, 22, 45
        sum_ += i
        # 0 + 33 == 33
        # 33 + 22 == 55
        # 55 + 45 == 100
        print(sum_)

    return sum_


sumUp(sampleList)






# Unique elemanlari donduren fonksiyonu yaziniz;
nonUniquee = [1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8]


def nonUnique(a):
    myList = list(set(a))

    return myList


nonUnique(nonUniquee)






# Asagıidaki sekilde string degistiren bir fonksiyon yazmak istiyoruz;

# Before = "hi my name is john and i am learning python"
# After = "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""

    for index in range(len(string)):
        if index % 2 == 0:
            new_string += string[index].upper()
        else:
            new_string += string[index].lower()
    return new_string


alternating("hi my name is john and i am learning python")


# Yukarıdaki soruyu "enumerate" kullanarak cozersek;
def alternating(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string


alternating("hi my name is john and i am learning python")






# For dongusu kullanarak arguman olarak girilen sayinin, faktoriyelini hesaplayan fonksiyonu yaziniz; *****
for i in range(5):
    print(i + 1)


def faktoriyel(value):
    a = 1
    for i in range(value, 0, -1):
        a *= i
    return a


faktoriyel(5)


def faktoriyel(value):
    a = 1
    for i in range(value):
        a *= (i + 1)
    return a


faktoriyel(3)






# Bonus: iceri istedigin kadar arguman girebildigin bir fonksiyonda girdigin tum sayilari toplayan fonksiyonu yaziniz.
def function(*args):
    num = 0

    for i in args:
        num = num + i

    return num


function(1, 2, 3, 20, 30, 50)






# fruits listesinde kelime uzunlugu 5'den kucuk olanlari getir;
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

liste = []
for i in fruits:
    if len(i) < 5:
        liste.append(i)

liste

fruitss = [i for i in fruits if len(i) < 5]
fruitss






# Hitters veri setinde int64 tipindeki degiskenleri getir;
import pandas as pd

df = pd.read_csv("datasets/hitters.csv")
df.info()

df.columns

liste = [col for col in df.columns if df[col].dtype == "int64"]
liste


# Hitters veri setinde object tipindeki degiskenleri getir;
import pandas as pd

df = pd.read_csv("datasets/hitters.csv")
df.info()

liste = [col for col in df.columns if df[col].dtype == "O"]


# Tum degiskenlerde gez, object tipindekileri buyuk harfle yaz;

liste = [col.upper() if df[col].dtype == "O" else col.lower() for col in df.columns]
liste



# [ if Sonuç if koşul  else elseSonuç for i in ... ]

# [ if Sonuç for i in ...  if koşul]