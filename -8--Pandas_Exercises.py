import pandas as pd
import numpy as np
import seaborn as sns

print("#################  GOREV 1  #################\n")
## """Seaborn kutuphanesi icerisinden Titanic veri setini tanimlayiniz."""
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df = sns.load_dataset("titanic")
print(df.head(), "\n", df.shape)



print("#################  GOREV 2  #################\n")
## """Titanic veri setindeki kadin ve erkek yolcularin sayisini bulunuz."""
print(f"Kadın ve Erkek Yolcuların Sayısı:\n{df['sex'].value_counts()}")

#ya da cinsiyere gore ayri ayri gormek istersek;
male_count = df['sex'].value_counts()['male']
print(f"Erkek Yolcu Sayisi:\n{male_count}")
female_count = df['sex'].value_counts()['female']
print(f"Kadin Yolcu Sayisi:\n{female_count}")



print("#################  GOREV 3  #################\n")
## """Her bir sutuna ait unique degerlerin sayisini bulunuz."""
print(f"Her bir sutuna ait unique degerleri:\n{df.nunique()}")

# ya da;
for i in df.columns:
    df[i].nunique()
    print(f"{i}\nunique deger sayisi:{df[i].nunique()}")



print("#################  GOREV 4  #################\n")
## """pclass degiskeninin unique degerlerini bulunuz."""
print(f"pclass degiskeninin unique degerleri: {df['pclass'].unique()}")

# ya da;
df.loc[:,"pclass"].unique()



print("#################  GOREV 5  #################\n")
## """pclass ve parch degiskenlerinin unique degerlerinin sayisini bulunuz."""
print(f"pclass ve parch degiskenlerinin unique deserleri:\n{df[['pclass', 'parch']].nunique()}")



print("#################  GOREV 6  #################\n")
## """embarked degiskeninin tipini kontrol ediniz. Tipini category olarak degistiriniz ve tekrar kontrol ediniz."""
print(f"embarked icin veri tipi:\n{df['embarked'].dtype}")
print(f"embarked icin yeni veri tipi:\n{df['embarked'].astype('category')}")

# Tekrar sorgulayalim;
str(df["embarked"].dtype)
df.info()



print("#################  GOREV 7  #################\n")
## """embarked degeri C olanların tum bilgelerini gosteriniz."""
print(df.loc[df["embarked"] == "C"])

# ya da;
print(df[df['embarked'] == 'C'])



print("#################  GOREV 8  #################\n")
## """embarked degeri S olmayanlarin tum bilgelerini gosteriniz."""
print(f"embarked degeri S olmayanlar:\n{df.loc[df['embarked'] != 'S']}")

# ya da;
print(f"embarked degeri S olmayanlar:\n{df[df['embarked'] != 'S']}")

# ya da;
df[~(df["embarked"] == "S")]["embarked"].unique()

a = df[df["embarked"] != "S"]
a["embarked"].unique()



print("#################  GOREV 9  #################\n")
## """Yasi 30 dan kucuk ve kadin olan yolcularin tum bilgilerini gosteriniz."""
print(f"Yası 30 dan kucuk ve kadin olan yolcular:"
      f"\n{df.loc[(df['age'] < 30) & (df['sex'] == 'female')].head()}")

# ya da;
df[(df["age"]<30) & (df["sex"]=="female")].head()



print("#################  GOREV 10  #################\n")
## """Fare'i 500'den buyuk veya yasi 70’den buyuk yolcularin bilgilerini gosteriniz."""
print(f"Fare'i 500'den buyuk veya yasi 70’den buyuk yolcular:"
    f"\n{df.loc[(df['fare'] > 500) | (df['age'] > 70)].head()}")

# ya da;
df[(df["fare"] > 500 ) | (df["age"] > 70 )].head()



print("#################  GOREV 11  #################\n")
## """Her bir degiskendeki bos degerlerin toplamini bulunuz."""
print(f"Her bir degiskendeki bos degerlerin toplami:\n{df.isnull().sum()}")



print("#################  GOREV 12  #################\n")
## """who degiskenini dataframe’den cikariniz."""
print(df.drop(columns="who", axis = 1, inplace=True)) # inplace=True ile degisikligin kaliciligini sagladik.

# ya da;
# print(f"{df.drop('who', axis = 1).head()}\nwho degiskeni dataframe'den cikarildi.")



print("#################  GOREV 13  #################\n")
## """deck degiskenindeki bos degerleri deck degiskenin en cok tekrar eden degeri (mode) ile doldurunuz"""
df["deck"].fillna(df["deck"].mode().iloc[0], inplace=True)
print(f"Bos deger sayisi:{df['deck'].isna().sum()}")

# ya da;
deck_mode = df['deck'].mode()[0]
df["deck"].fillna(deck_mode, inplace=True)
print(f"Bos deger sayisi:{df['deck'].isna().sum()}")



print("#################  GOREV 14  #################\n")
## """age degiskenindeki bos degerleri age degiskeninin medyani ile doldurunuz."""
print(df["age"].fillna(df["age"].median(), inplace=True))
print(f"Bos deger sayisi:{df['age'].isna().sum()}")


print("#################  GOREV 15  #################\n")
## """survived degiskeninin pclass ve cinsiyet degiskenleri kirilimininda sum, count, mean degerlerini bulunuz."""
df.groupby(["sex", "pclass"]).agg({"survived": ["sum", "count", "mean"]})



print("#################  GOREV 16  #################\n")
## """30 yasın altinda olanlar 1, 30'a esit ve ustunde olanlara 0 verecek bir fonksiyon yazin.
# Yazdiginiz fonksiyonu kullanarak titanik veri setinde age_flag adinda bir degisken olusturunuz olusturunuz. (apply ve lambda yapilarini kullaniniz)"""
def age_30(age):
    if age<30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)



print("#################  GÖREV 17  #################\n")
## """Seaborn kutuphanesi icerisinden Tips veri setini tanimlayiniz."""
tips_df = sns.load_dataset("tips")
print(f"tips veri seti:\n{tips_df.head()}")

print("#################  GÖREV 18  #################\n")
## """Time degiskeninin kategorilerine (Dinner, Lunch) gore total_bill degerinin sum, min, max ve mean degerlerini bulunuz."""
tips_df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

print("#################  GÖREV 19  #################\n")
## """Day ve time’a gore total_bill degerlerinin sum, min, max ve mean degerlerini bulunuz."""
tips_df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

print("#################  GÖREV 20  #################\n")
## """Lunch zamanina ve kadin musterilere ait total_bill ve tip degerlerinin day'e göore sum, min, max ve mean degerlerini bulunuz."""
tips_df[["total_bill", "tip", "day"]].loc[(tips_df["time"] == "Lunch") & (tips_df["sex"] == "Female")].groupby("day").\
    agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})

# ya da ayri ayri gormek istersek;
lunch_female_df = tips_df.query("time == 'Lunch' & sex == 'Female'")
print(f'sum:\n{lunch_female_df[["day", "total_bill", "tip"]].groupby("day").sum()}\n')
print(f'min:\n{lunch_female_df[["day", "total_bill", "tip"]].groupby("day").min()}\n')
print(f'max:\n{lunch_female_df[["day", "total_bill", "tip"]].groupby("day").max()}\n')
print(f'mean:\n{lunch_female_df[["day", "total_bill", "tip"]].groupby("day").mean()}\n')



print("#################  GÖREV 21  #################\n")
## """size'i 3'ten kucuk, total_bill'i 10'dan buyuk olan siparislerin ortalamasi nedir? (loc kullaniniz)"""
tips_df.query("size < 3 & total_bill > 10").loc[:, "total_bill"].mean()

# ya da ayri ayri tip ve size degerlerini de gormek istersek;
tips_df.loc[(tips_df["size"] < 3) & (tips_df["total_bill"] > 10)].mean()



print("#################  GÖREV 22  #################\n")
## """total_bill_tip_sum adinda yeni bir degisken olusturunuz. Her bir musterinin odedigi totalbill ve tip'in toplamini versin."""
tips_df["total_bill_tip_sum"] = tips_df["total_bill"] + tips_df["tip"]



print("#################  GÖREV 23  #################\n")
## """Total_bill degiskeninin kadin ve erkek icin ayri ayri ortalamasini bulunuz.
# Buldugunuz ortalamalarin altinda olanlara 0, ustunde ve esit olanlara 1 verildigi yeni bir total_bill_flag degiskeni olusturunuz.
# Kadinlar icin Female olanlarinin ortalamalari, erkekler icin ise Male olanlarin ortalamalari dikkate alinacaktir.
# Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak baslayiniz. (If-else kosulları icerecek)"""
a = tips_df["total_bill"].loc[tips_df["sex"] == "Female"].mean()
b = tips_df["total_bill"].loc[tips_df["sex"] =="Male"].mean()

def func(sex, total_bill):
    if sex=="Female":
        if total_bill < a:
            return 0
        else:
            return 1
    else:
        if total_bill < b:
            return 0
        else:
            return 1

tips_df["total_bill_flag"] = tips_df[["sex","total_bill"]].apply(lambda x: func(x["sex"],x["total_bill"]),axis=1)



print("#################  GÖREV 24  #################\n")
## """total_bill_flag degiskenini kullanarak cinsiyetlere gore ortalamanin altinda ve ustunde olanlarin sayisini gozlemleyiniz."""
tips_df.loc[tips_df["total_bill_flag" == 0].value_counts()
tips_df[["sex"]].loc[tips_df["total_bill_flag"] == 0].value_counts()

# ya da;
tips_df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag":"count"})



print("#################  GÖREV 25  #################\n")
## """Veriyi total_bill_tip_sum degiskenine gore buyukten kucuge siralayiniz ve ilk 30 kisiyi yeni bir dataframe'e atayiniz."""
tips_df["total_bill_tip_sum"].sort_values(ascending = False).head(30).head()

# Bu yalnizca secilen sutunu siralar oysa biz dataframe' i "total_bill_tip_sum" e gore siralamak istedigimiz icin asagidaki gibi ilerlemeliyiz.
tips_df.sort_values(by = ["total_bill_tip_sum"], ascending = False).head(30).head()

# ya da;
tips_df.sort_values("total_bill_tip_sum", ascending = False).head(30).head()

# ya da;
new_df = tips_df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape