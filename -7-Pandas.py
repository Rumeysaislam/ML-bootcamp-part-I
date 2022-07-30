### PANDAS ###

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)                   # IIk 3 değer ve index bilgileri
s.tail(3)                   # Son 3 değer ve index bilgileri



# Veri Okuma (Reading Data);
df = pd.read_csv("advertising.csv")
df.head()



# Veriye Hızlı Bakış (Quick Look at Data);
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()                   # Ilk 5 indexteki veriler
df.tail()                   # Son 5 indexteki veriler
df.shape                    # Boyut bilgisi
df.info()
df.columns                  # Degiskenler (Sutun degerleri)
df.index                    # Baslangıc, bitis index degeri ve index artis miktari
df.describe().T             # İstatistiksel dagilim degerleri
df.isnull().values.any()    # Eksik deger var mı?
df.isnull().sum()           # Degiskenlerdeki toplam eksik deger sayisi
df["sex"].head()            # "sex" degiskeninin ilk 5 degeri
df["sex"].value_counts()    # "sex" degiskeninin degerlerinin sayisi
df["sex"].count()           # "sex" degiskeninin toplam deger sayisi



# Pandas'ta Seçim İşlemleri (Selection in Pandas);
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)       # Cıktıda tum degiskenleri gormek icin yaptik bu ayari.
pd.set_option('display.width', 500)              # Tüm veri setinin yan-yana olmasini istiyorum.
df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]                                         # 0'dan 13'e kadar olan index degerleri
df.drop(0, axis = 0).head()                      # 0. indexteki satiri sildim

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis = 0).head(10)       # Verilen indexlerdeki satirlari sildim.

# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)



# Değişkeni Indexe Çevirmek ;Yaş değiskenini indexe degistirelim;
df["age"].head()                           # df["age"].head() = df.age.head() : ikisi de " degisken secim islemi" icin kullanilabilir.
df.age.head()

df.index = df["age"]                      #V eri setinin index bilgisini, yas degiskenine atadik. Yas bilgisi bir degisken olarak indexe eklendi.

df.drop("age", axis = 1).head()           # indexe ekleyince degisken olarak ihtiyacimiz yok "drop" ile siliyoruz.
                                          # axis = 1 : silme işleminin sütunlardan oldugunu ifade ediyoruz.
                                          # Kalici bir degisiklik olmasini istemedigimiz icin yeni bir atama yapmadik ya da "inplace" kullanmadık.
                                          # Index bolumunde artik yas bilgileri var.
df.drop("age", axis=1, inplace = True)    # Kalici degisiklik (inplace=True) yapiyoruz. Yas degiskeni artik indexte.
df.head()



# Indexi Değişkene Çevirmek;
df.index

df["age"] = df.index        # indexi dataframe'e atiyoruz.
                            # df["age"] degiskeni secerken bu ifade df icinde yoksa, yeni degisken eklendigi anlasilir.
                            # Yas degiskeni, degisken olarak eklendi.

df.head()
df.drop("age", axis = 1, inplace = True)  # ikinci yolu denemek icin sildik;

df.reset_index().head()                   # indexte yer alan degeri silip, sutun bazinda degisken olarak ekleyecektir.
df = df.reset_index()
df.head()


# Değişkenler Üzerinde İşlemler;
# Sutun bazinda yani degiskenler uzerinde islemler;


"age" in df                 # Degisken varligini sorguladik.

df["age"].head()            # Degiskeni sectik.
df.age.head()

df["age"].head()
type(df["age"].head())      # Sectigimiz degiskenin tipini sorguladik; Pandas.Series


df[["age"]].head()          # !!! Secimin df kalmasını istiyorsak [["..."]] yapmaliyiz.
type(df[["age"]].head())    # Artik Pandas.Series degil, "dataframe"

df[["age", "alive"]]        # Bir df icinden birden fazla degisken secme


# Daha fazla degisken secmek icin, liste gondermemiz lazım;
col_names = ["age", "adult_male", "alive"]
df[col_names]               # Degiskenleri veri seti icerisinden sectik.


# Veri setine var olan degisken uzerinden yeni degisken ekliyoruz;
df["age2"] = df["age"]**2                 # df' de olmayan bir degisken ismi yazarsak o degiskeni eklemis oluruz.
df["age3"] = df["age"] / df["age2"]

df.head()

df.drop("age3", axis = 1).head()          # "drop" ile sütun bazli (axis= 1) degisken sildik.

df.drop(["age", "adult_male", "alive"], axis = 1).head()
df.drop(col_names, axis = 1).head()       # Coklu degisken silme


### Belirli bir string ifadeyi barındıran degiskenleri silmek istiyorum;
df.loc[:, df.columns.str.contains("age")].head()

#loc: label base secim yapmak icin kullanilir.
# [: , ...] Butun satirlari sectik, sutunlarla ilgili islem yapiyorum.
# bu df'in sutunlarındaki degiskenlere bir string operasyonu yapacagim.
# "contains" : stringlere uygulanan bir method. Verilen string ifadeyi, ondan onceki sgtringde arar.
# Boylelikle "age" barindiranlari secmis olduk.

df.loc[:, ~df.columns.str.contains("age")].head()
# "~" kullanılarak "degildir" anlami verilir. Yani "age" barindirmayanlari secmis olduk.





# ILOC & LOC

# loc ve iloc: df'lerde secme islemi icin kullanilan ozel yapilardir.


# iloc: integer based selection ; index bilgisi icererek secim yapma " -e kadar"
df.iloc[0:3]                # 0'dan 3'e kadar (3 dahil degil) sectik.
df.iloc[0, 0]               # 0. satir, 0. sutundaki elemani sectik.

# loc: label based selection ; mutlak olarak indexlerdeki labellara gore secim yapar. "dahil"
df.loc[0:3]                 # 0, 1, 2 ,3. elemanları secti. Label yani etiket nasilsa onu mutlak olarak secer.

# Aradaki farki anlamak icin;
df.iloc[0:3, 0:4]           # Satirlarda 0'dan 3'e gitmek istiyorum.
df.iloc[0:3, "age"]         # Hata verir, integer bilgi bekler.

df.loc[0:3, "age"]


# Bazı degiskenleri secmek istedigimizde;
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]



# Koşullu Seçim (Conditional Selection);

# Veri setinde yasi 50'den buyuk olanlari secmek istiyorum;
# Kosulu ve kosulun hangi degiskene uygulanacagi bilgisini girdik;
df[df["age"] > 50].head()

# Yasi 50'den buyuk kac kisi var?
df[df["age"] > 50].count()                       # Ciktida karisiklik var cunku secim islemi yapmadik.
df[df["age"] > 50]["age"].count()

# Yasi 50'den buyuk olan kisilerin class bilgilerini ogrenmek istedigimde;
df.loc[df["age"] > 50, ["age", "class"]].head()  # Bir kosul + iki sutun secmis olduk.

# Yasi 50'den buyuk erkekleri secmek istiyorum; " iki kosul + iki sutun"
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
# Kosullar parantez icerisine alinir ve "&" ile baglanir.

# 3. kosulu eklersem;
# embark_town: Yolculuk icin gemiye binilmesi gereken limani ifade ediyor.
df["embark_town"].value_counts()

df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"), ["age", "class"].head()

# Degisken bilgisisine de erismek icin;
df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg")),
       ["age", "class", "embark_town"]].head()

df["embark_town"].value_counts()

# embark'dan iki sinifa erismek istersek (" ya da ");
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()





# TOPLULASTIRMA ve GRUPLAMA (Aggregation & Grouping)

# Toplulastirma : Verileri toplu bir sekilde temsil etmek. Orn.: Ozet istatistik

# Betimleme, Toplulastirma fonksiyonlari; ("group by" ile hepsini kullanabiliriz (pivot table haric).)
# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Kadinlarin ve erkeklerin yas ortalamasina erismek istiyorum;

df["age"].mean()                   # Yas ortalamasi

# Cinsiyete gore yas ortalamasini grupladik: Cinsiyete gore "group by" islemi yapiyoruz;
df.groupby("sex")["age"].mean()    # Yas degiskeninin ortalamasini aldik.

# Sadece ort. degil toplamini da ogrenmek istiyorum; (agg.: aggregation)
df.groupby("sex").agg({"age": "mean"})              # Yas degiskeninin ortalamasini aldik. Bu kullanim onemli cunku agg ile birden cok fonk. kullanabiliyoruz.. (*)
df.groupby("sex").agg({"age": ["mean", "sum"]})     # Veriyi cinsiyete gore kirdik. Yasin ort. ve toplamini elde ettik.

# Cinsiyete gore kirdiktan (group by) yaptiktan sonra liman bilgisi degiskeninin frekansini da elde etmek istiyoruz;
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "embark_town": "count"})     # Cikti embarkin frekansı degil, embark'a gore cinsiyetin frekansi.


# Sayisal degiskeni degerlendirelim;
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

# Diger bazi kategorilere gore de kirilim yapmak istersem; liste formunda group by yaptik.
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

# class bilgisini de boyut olarak eklemek istersek;
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})

# Cinsiyet degiskeninin frekans bilgisini de eklersek;
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})





# PIVOT TABLE;
# Ozet istatistigi kirilimlara gore gormemizi saglar.
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# 1.deger: Kesisimlerde neyi gormek istedigim, 2.deger: satırda indexte gormek istedigim, 3.deger: sütunda gormek istedigim.
df.pivot_table("survived", "sex", "embarked")
# Survived'ın ortalamasi geldi. Cunku pivot table'in on tanimli degeri mean()'dir.

# aggregation function argumanını bicimlendirerek sekillendirebiliriz;
df.pivot_table("survived", "sex", "embarked", aggfunc="std")

# Daha fazla boyut bilgisini ekleyebilmek icin;
df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()
# Sutunlarda iki index satirlarda tek index var.


# Hem cinsiyet kirilimi, hem gemiye binilen lokasyonu, yaslara gore de bir kirilim istiyorum;

# Veri setindeki yas degiskeni sayisal bir degisken. Kategorik degiskene cevirmeliyiz;
### cut ve qcut: Sayisal degiskeni kategorik degiskene cevirmek icin kullanilir.
#### cut: sayisal degiskeni belli degerlere gore bolme,
#### pcut: sayisal degiskeni (tanimayip veya bilerek) ceyrekliklere gore bolunmesini istersem (otomatik siralar);

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", "new_age")
# 1.deger: Kesisimlerde neyi gormek istedigim, 2.deger: satırda indexte gormek istedigim, 3.deger: sütunda gormek istedigim.

# Boyut eklemek istersem;
df.pivot_table("survived", "sex", ["new_age", "class"])





# APPLY ve LAMBDA
#############################################
# Apply: Satir veya sutunlarda otomatik olarak fonk. calistirmayi saglar.
# Lambda: Fonksiyon tanimlama seklidir. def'ten farki kullan-at fonksiyonu olmasidir. Yani kod akisi esnasinda bir kere kullaniyoruz.

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

#Yas degiskeni üzerinden iki yeni degisken olusturuyoruz;
df["age2"] = df["age"]*2
df["age3"] = df["age"]*5
df.head()

# Yas degiskenlerini'a bolmek istiyoruz;
df["age"]/10.head()         # hata verir, parantez icine alacagiz.

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

## Donguyle yazmak istersek; (Degiskenlere fonk. uygulamak istiyorum.)
for i in df.columns:
    if "age" in i:
        print(i)

for i in df.columns:
    if "age" in i:
        print((df[i]/10).head())

# Simdiye kadar sadece print ettik kaydetmedik;
for i in df.columns:
    if "age" in i:
        df[i] = df[i]/10   # Sectigimiz degiskeni 10'a bolup sectigimiz degiskene atadik.

df.head()

### apply ve lambda kullanarak yapmak istersek;
df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# Programatik sekilde yas degiskenini secmek istersek;

# Butun satırları ve sütunlardan yas degiskeni barindiranlari secip fonksiyonu uyguluyoruz;
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

# Daha programatik yazmak istersek; :D
# !!! Bir degiskendeki degerleri standartlastirmak istiyoruz;
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# lambda ile dongu yapmadan degiskenleri secebildik ve fonksiyonu uyguladik.

# apply ile sadece lambdayı değil, klasik fonksiyonlarimizi da kullanabiliriz;
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# Islemleri kaydetmek icin;
# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# Daha otomatik kaydetmek icin; :D
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
# Sol tarafta istedigim yeri sectim, sag tarafta istedigim yere fonksiyon uyguladim.
df.head()




# BIRLESTIRME (Join) ISLEMLERI

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))                   # 1 ile 30 arasinda 5*3 lük np.array'i olusturduk.
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])     # 3 sutun oldugu icin 3 degisken tanimladik.
df2 = df1 + 99                                              # df'e 99 ekleyerek 2. df olusturduk.

# "concat" ile birlestirme; !! Liste icerisinde ifade ediyoruz.
pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)
# ignore_index=True : Var olan indexleri gormezden gelip yeniden siraladik.




# MERGE ile Birleştirme İslemleri

# pd.DataFrame: Bana bir veri ver onu DataFrame'e ceviririm. :)

# Calisanlar ve calistiklari departmanlri gosteren df;
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

# Calisanlar ve calisanlarin ise baslangic tarihleri; ( Dort farkli veri yapisindan bir df olusturulmustur.)
df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})


# Bu iki veriyi birlestirmek istiyorum;
pd.merge(df1, df2)  # Bu da calisir,
pd.merge(df1, df2, on="employees")
# on="employees": calisanlara gore birlestirme islemi yapmak istedigimizi soyledik.

# Amaç: Her calisanin mudurunun bilgisine erismek istiyoruz;
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)

# join yani birlestirme islemleri veri tabaninda yapilir ve python tarafina aggrige edilmis ve tekillestirilmis tablolar getirilir.
# Yani gozlem birimleri acisindan tekillestirilmis ve toplulastirilmis degerler getirir.