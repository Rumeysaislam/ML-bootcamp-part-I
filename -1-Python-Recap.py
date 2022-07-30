# Python
# Veri Yapıları (Data Structures)

# SAYILAR

# int
a = 5
type(a)

# float
b = 5.5
type(b)

# complex
c = 2j + 4
type(c)

# Islem  yapalim;
int(a + b)
print(a + b)

# Boolean; (True-False)
True
type(False)

1 == 1
1 == 2

2 > 3
2 < 3

2 >= 2
2 <= 2


## LISTE (List)

x = ["a", "b", "c"]
x
type(x)


x[0]
# Degistirilebilir.
x[0] = "x"
x


# Siralidir. Index islemleri yapilabilir.
x[0]
x[1]


# Kapsayicidir. Icinde birden fazla veri yapisi bulundurabilir.
liste = ["a", 2, 3.5, True]


### Liste Metodlari (List Methods)

dir(liste)                          # Uygulanabilecek metodlari goruruz.


# len: builtin python fonksiyonu, boyut bilgisi;
len(liste)


# append: eleman ekler;
liste.append(100)
liste


# pop: indexe gore siler;
liste.pop(0)
liste

liste.pop()                         # Son degeri sildik.
liste


# insert: indexe ekler;
liste
liste.insert(2, 99)
liste



## SOZLUK (Dictionary)

x = {"name": "Ahmet", "Age": 22}
x
type(x)


# Degistirilebilir.
x["name"] = "Rumeysa"
x


# Sirasizdir. (3.7'den sonra sirali. OrderedDict)
x[0]


# Kapsayicidir.
x = {"name": "Ahmet", "Age": 22}

# "Ahmet" = String / 22 = int


### Key Sorgulama;
"name" in x
"Ahmet" in x                    # False; value bu sekilde sorgulanmaz.


### Key'e Göre Value'ya Erismek;
dictionary = {("Ahmet", "Mehmet"): ["İstanbul", 20],
              ("Ayşe", "Fatma"): ["Ankara", 25],
              ("Mehmet", "Hasan"): ["İzmir", 30]}

type(dictionary)  # dic.

dictionary = {["Ahmet", "Mehmet"]: ["İstanbul", 20],
              ["Ayşe", "Fatma"]: ["Ankara", 25],
              ["Mehmet", "Hasan"]: ["İzmir", 30]}

type(dictionary)  # Error

# Sözlükteki "key" değerleri sabit veri yapıları olmak zorunda olduğundan "liste" olamazlar ama "tuple" olabilirler. (*)

dictionary = {"Ahmet": ["İstanbul", 20],
              "Ayşe": ["Ankara", 25],
              "Mehmet": ["İzmir", 30]}

dictionary["Ahmet"]

dictionary["Ahmet"][0]
# ya da;
dictionary.get("Ayşe")


### Value Degistirmek;
dictionary["Ahmet"] = ["Antalya", 22]
dictionary


### Tum Key'lere Erismek;
dictionary.keys()


### Tum Value'lara Erismek;
dictionary.values()


### Key-Value Degerini Guncellemek;
dictionary
dictionary.update({"Mehmet": ["Tekirdağ", 40]})
dictionary

dictionary.update({"Akın": ["Bursa", 30]})
dictionary
# Olmayan key'e atama yaparsak, bunu sozluge ekler.


### Yeni Key-Value Eklemek;
dictionary.update({"Samet": ["İstanbul", 35]})
dictionary



## DEMET (Tuple)

x = ("a", "b", "c")
x
type(x)


# Degistirilemez. LISTELERDEN FARKI BUDUR. (Mulakat Sorusu)
x[0] = "x"


# Siralidir.
x[0]


# Kapsayicidir.
x = ("a", 5, 2.5)


# Mülakat Sorusu
# Tuple ile Listenin Farkı nedir?
"""
Tuple'ın değiştirilemez, Liste'nin değiştirilebilir olması.
"""


# Mülakat Sorusu
# Tuple'ı hangi durumlarda listenin yerine tercih ederiz?
"""
Değiştirilmemesi gereken veriler tutuyorsanız tuple tercih etmelisiniz.
"""

# Bilgi:
# Tuplelar Listelerden daha verimlidir;
# Herhangi bir elemanı değiştirememe haricinde eleman ekleyip çıkaramazsınız da dolayısıyla ramde ekstra yer tutmuyor hiçbir zaman.



## Set

t = set([1, 2, 3])
type(t)
# ya da;
x = {"x", "y", "z"}
x
type(x)


# Degistirilebilir;
x.add(2)                            # Tek eleman ekleme
x.update([3, 4, 5])                 # Birden fazla eleman ekleme
x

x.discard(2)
x.remove(3)
x

# Farklari ne?

x.discard(8)                        # 8 elemani yok ama uyari vermez
x.remove(8)                         # Error


# Sirasiz + Essizdir;
x[0]
x
x.update([4, 4, 4, 4, 4])           # Essiz; sadece bir tane 4 ekler.
x


# Kapsayicidir;
x = {1, "a", 2.5}



## difference(): Iki kumenin farkı;

set1 = {1, 3, 5}
set2 = set([1, 2, 3])


# set1'de olup set2'de olmayanlar;
set1.difference(set2)
set1 - set2


# set2'de olup set1'de olmayanlar;
set2.difference(set1)
set2 - set1


# intersection(): Iki kumenin kesisimi;
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.isdisjoint(set2)                   # Kesisimin bos olup olmadigini sorguladik.

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


# union(): Iki kumenin birlesimi;
set1.union(set2)
set2.union(set1)




# KARAKTER DIZILERI (Strings)

name = "Rumeysa"
name = 'Rumeysa'

print("Hello 'Rumeysa'")
print('Hello "Rumeysa"')


## Cok Satirli Karakter Dizileri;
long_str = """Seyahat etmeyenler.
Yavaş yavaş ölürler
Okumayanlar, müzik dinlemeyenler,
Vicdanlarında hoşgörüyü barındıramayanlar.
"""

print(long_str)


## Karakter Dizilerinin Elemanlarına Erismek;
name
name[0]
name[1]

name[-1]                                  # Sondaki index


## Karakter Dizilerinde Slice İslemi;
name[0:2]

long_str[0:10]


## String Icerisinde Karakter Sorgulamak;
long_str

"Seyahat" in long_str
"seyahat" in long_str                    # Buyuk-kucuk harf duyarlidir.
"öl" in long_str



# String (Karakter Dizisi) Metodları

dir(str)                                # Uygulanilecek metodlari gorduk.


# len;
name = "Rumeysa"
type(name)

len(name)

len("Rumeysa")


# upper() & lower(): Kucuk-buyuk harf donusumleri;
"RUMEYSA".lower()
"rumeysa".upper()

"RUMEYSA".replace("U", "A").lower()


vbo = "verı bılımı okulu"
vbo.replace("ı", "i", 3)                # Ilk 3 "ı" harfini "i" yaptik.
vbo.replace("ı", "i", 2)


# replace: karakter degistirme;
isim = "Rumeysa"
isim = isim.replace("u", "a")           # Kalici degisklik icin yeniden atama yapmak gerekir.


# split: boler;
isim.split()


# strip: kirpar;
isim = "**rumeysa**"
isim
isim.strip("*")                         # Sadece soldakini kaldirma.

isim.rstrip("*")                        # Sadece sagdakini kaldirma.


# capitalize: ilk harfi buyutur;
"pablo".capitalize()

"pablo".startswith("w")                 # "w" ile mi basliyor? True veya False dondurur.

"Pablo".startswith("p")                 # Buyuk, kucuk harf duyarlı.




# FONKSİYONLAR (FUNCTIONS)

def selam():                            # Arguman almayip direkt print ettik.
    selam = "selamlar"
    print(selam)
    return selam


kelime = selam()
kelime


def seslen(kelime):                     # Arguman alan fonksiyon yazarsak;
    return kelime


seslen("hey")

kelime = seslen("hey")
kelime

kelime = seslen("merhaba")

kelime


def seslen(kelime):
    print("kelimeyi kaydediyorum...")
    return kelime


# return'dan sonra kelimeyi yakalayip uzerinde string islem yapabiliyoruz. Sadece print ile bunu yapamayiz. (*)

kelime = seslen("Hey")
kelime

kelime * 5

seslen("Hey") * 5
seslen("Hey").upper()


def toplama(a, b):
    return (a + b)


a = toplama(3, 2)
a * 5


def seslenis():
    return ("merhaba")


seslenis()

b = seslenis()
b * 5


# return, fonksiyonda bir tane olur.
# return a, b, c... diye de kullanilabilir.



# Şimdiki yıl ve dogum yılı bilgilerini argüman olarak alan ve yaşı hesaplayan fonksiyonu yazarsak;
def age(curr_year, birth_year):
    agee = curr_year - birth_year
    return agee                       # print ile yapsaydik donduremezdik.


yas = age(2022, 2000)

yas * 5


def age(current_year, birth_year):
    print(current_year - birth_year)


age(2022, 2000)

yas = age(1996, 2022)
yas * 5                             # Hata verir cunku sadece "print" ettik; "return" etmedik.



# On tanımlı argüman/parametre;
def age(current_year=2022, birth_year=2000):
    print(current_year - birth_year)


age()
age(2000, 1980)                    # On tanimli olsa da bu sekilde deger degistirebiliyoruz.



# Fonksiyon Icerisinden Fonksiyon Cagirmak;
def age(current_year, birth_year):
    return current_year - birth_year


def sigorta(current_year, birth_year, Work_year):
    yas = age(current_year, birth_year)
    year = current_year - Work_year
    return yas * year


sigorta(2022, 2000, 2018)

"""
def age(current_year=2022, birth_year= 1996):
    print(current_year - birth_year)

Bu fonksiyon ile cagirsaydik calismazdi.
"""



# DOCSTRİNG

def sum(arg1, arg2):
    """
    Sum of two numbers

    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    return arg1 + arg2


sayi = sum(3, 5)
sayi



# KOŞULLAR (CONDITIONS)

exam_notes = [10, 20, 30, 40, 50, 60, 70]


def passed(mark):
    if mark == 60:
        print("sinirda gectiniz")
    elif mark > 60:
        print("gectiniz")
    else:
        print("kaldiniz")


for i in exam_notes:
    passed(i)

[passed(i) for i in exam_notes]  # return edilmedgi icin [None, ... ] diye cikar.

mark = [20, 60, 50, 85, 70, 15, 5]
a = [print("Gecti") if i >= 60 else print("Kaldi") for i in mark]


def passed(mark):
    if mark == 60:
        print("sinirda gectiniz")
        return "sinıirda " + str(mark)
    elif mark > 60:
        print("gectiniz")
        return "gectin " + str(mark)
    else:
        print("kaldiniz")
        return "kaldin " + str(mark)


passed(70)
passed(60)
passed(40)

exam_notes = [10, 20, 30, 40, 50, 60, 70]

for i in exam_notes:
    passed(i)

[passed(i) for i in exam_notes]


## break & continue & while

names = ["a", "b", "c", "d", "e"]

for name in names:
    if name == "c":
        break
    print(name)

for name in names:
    if name == "c":
        continue
    print(name)


# while;
number = 1

while number < 20:                   # Bu condition dogruysa, calisir.
    print(number)
    number += 1

# Enumerate: Otomatik Counter/Indexer ile for loop (index saymami saglar.)


names = ["ahmet", "mehmet", "rumeysa", "cemal"]

for i in names:
    print(i)

for i, name in enumerate(names):
    print(i)

for i in enumerate(names):
    print(i)

for i, name in enumerate(names):
    print(i, name)

for i, name in enumerate(names):
    print(i + 1, name)                 # Sifirdan degil de birden baslatmak icin boyle yazariz.


# lambda;
def sum(a, b):
    return a + b


sum(1, 3)

# Fonksiyonu lambda ile yazmak istersek;
new_sum = lambda a, b: a * b

new_sum(4, 5)