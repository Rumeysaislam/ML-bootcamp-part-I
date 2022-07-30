### Neden NumPy?
#############################################
import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

## Numpy; Sabit tipli (fixtype) veri saklanır (arraylar uzerinde daha hizli calismayi saglar.)
#         Vektorel operasyonlardir (Daha az cabayla daha fazla islem yapar.)

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b


### NumPy Array'i Olusturmak (Creating Numpy Arrays);
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

# Girilen sayi adadince 0 yazdirmak icin;
np.zeros(10)
np.zeros(10, dtype=int)                                 # Float olan tipi int'e cevirdik.

# 1 lerden olusan dizi olusturmak icin;
np.ones((3, 5), dtype = int)

# 0 ile 10 arasinda 10 tane sayi yazdirmak istersek;
np.random.randint(0, 10, size = 10)
np.random.randint(0, 10, 10)

# Istedigimiz "dagilim ozelliklerinde" array olusturmak icin;
np.random.normal(10, 4, (3, 4))                         # 10: ortalama sapma, 4: standart sapma (3, 4): boyut bilgisi

np.random.randint(0, 1, 10)                             # Out: array,([0, 0, 0,...]); Cunku rand"int"
np.linspace(0, 1, 10)                                   # 0 ile 1 arasında 10 sayı yazdirdik.

# Sadece belli sayidan olusan array yazmak istersek;
np.full((3,5), 3)                                       # (3, 5) lik sadece 3'lerden olusan array

# "Dogrusal bir array" olusturmak icin;
np.arange(0, 31, 3)                                     # 0'dan 31'e kadar 3'er artan dizi



### NumPy Array Ozellikleri (Attibutes of Numpy Arrays);

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype

z = np.full((3, 5), 3)
z.ndim
z.shape
z.size
z.dtype


### Yeniden Sekillendirme (Reshaping);
np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)


### Array Birlestirme (Concatenation);
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.concatenate([x, y])
print(z)


## Iki Boyutta Birlestirme;

# Satir bazinda birlestirme;
a = np.array([[1, 2, 3], [4, 5, 6]])                    # Iki boyutlu np.array
b = np.array([[3, 5, 7],
              [2, 4, 6]])

c = np.concatenate([a, b])
print(c)

# ya da;
c = np.concatenate([a, b], axis=0)
print(c)

# Sutun bazinda birlestirme;
a = np.array([[1, 2, 3], [4, 5, 6]])                    # Iki boyutlu np.array
b = np.array([[3, 5, 7],
              [2, 4, 6]])

c = np.concatenate([a, b], axis=1)
print(c)


### Array Ayirma (Splitting);
x = np.array([1, 2, 3, 99, 99, 3, 2, 1])
t = np.split(x, [3, 5])                                 # (Neyi, [kacıncı indexlerde ayiracaksan])
print(t)

x = np.array([1, 2, 3, 99, 99, 3, 2, 1, 100, 56, 62])
z = np.split(x, [3, 5, 7])
print(z)


### Array Siralama (Sorting);
v = np.array([2, 4, 6, 3, 1])
v.sort()                                                # Kalici degisiklik yapar !
print(v)

# İki boyutlu arraylerde siralama;
m = np.random.normal(20, 5, (3, 3))                     # Dagilim ozelliklerine gore array olusturduk; 20: ort, 5: standart sapma
n = np.sort(m, axis=0)                                  # Her bir satiri kendi icinde kucukten buyuge siralar.
t = np.sort(m, axis=1)                                  # Her bir sutunu kendi icinde kucukten buyuge siralar.

print(m)
print("\n\n", n, "\n\n", t)


### Index Seçimi (Index Selection);
a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999                                              # Sifirinci indexe yeniden atama yapmis olduk.


m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1, 1]
m[2, 3]

m[2, 3] = 999                                           # Yeniden atama yaptik.

m[2, 3] = round(2.9)                                    # Numpy "fixtype" oldugundan float olarak degil, int olarak ekledi. (*)
m[2, 3] = round(2.4)                                    # Atama yaparken 2.5 ve ustunu yukariya devreder, 2.5 altini asagiya devreder.

m[2, 3] = np.floor(2.9)                                 # Asagiya devreder.
m[2, 3] = np.ceil(2.1)                                  # Yukariya devreder.

m[:, 0]                                                 # Tum satirlari ve sifirinci sutunu al.
m[1, :]                                                 # 1.Satiri ve tum sutunlari al.
m[0:2, 0:3]                                             # Ilk iki satiri, ilk uc sutunu al.




### Fancy Index;
v = np.arange(0, 30, 3)
v[1]
v[4]

# Birden fazla elemana ayni anda erismek icin;
[v[1], v[3], v[5], v[2], v[6]]

# ya da "liste olusturarak" yapariz;
catch = [1, 2, 3]
v[catch]        # 1., 2. ve 3. elemani yakaladik.




### Numpy'da Koşullu İşlemler (Conditions on Numpy);
v = np.array([1, 2, 3, 4, 5])

## Klasik döngü ile;
ab = []
for i in v:
    if i < 3:
        ab.append(i)
print(ab)


cd = []
for i in v:
    if i >= 3:
        cd.append(i)
print(cd)


## Numpy ile;
v < 3

v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]



### Matematiksel İşlemler (Mathematical Operations);
v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

## Metodlar araciligiyle;
np.subtract(v, 1)   # Hepsinden 1 cikarttik
np.add(v, 1)        # Hepsine 1 ekledik
np.mean(v)          # Ortalama
np.sum(v)           # Toplam
np.min(v)           # Min deger
np.max(v)           # Max deger
np.var(v)           # Varyans

# Degisikliklerin kalici olmasi icin yeniden atama yapariz;
v = np.subtract(v, 1)



### NumPy ile İki Bilinmeyenli Denklem Çözümü;
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10
# Matematiksel ifadeyi NumPy'in anlayacagi formata ceviririz;

a = np.array([[5, 1], [1, 3]])                      # Katsayilar array'i; Katsayilari vektore koyuyoruz.
b = np.array([12, 10])                              # Sonuclar array'i; Sonuclari vektore koyuyoruz.

## Lineer cebir islemleri icin özellestirilmis "linalg" alt kutuphanesinden "solve" fonksiyonunu cagiririz;
c = np.linalg.solve(a, b)                           # 1. ve 2. arguman arasindaki iliski neticesinde olusacak olan katsayilari hesaplar.
print(c)