# List & Dict Comprehension Uygulamalar

# List Comprehension

### Bir Veri Setindeki Değişken İsimlerini Degistirmek;

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())


A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A


# Uzun uzun yazmak yerine, "Comprehension" kullaniriz;

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']



### Isminde "INS" olan degiskenlerin basina FLAG digerlerine NO_FLAG eklemek istiyoruz;

# Icerisinde "INS" olanlar;
[col for col in df.columns if "INS" in col]

# Icerisinde "INS" olanlara "FLAG_" ekle;
["FLAG_" + col for col in df.columns if "INS" in col]

# Icerisinde "INS" olanlara "FLAG_", olmayanlara "NO_FLAG" ekle;
["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']




# Dict Comprehension

### Amac; key'i string, value'su asagidaki gibi bir liste olan sozluk olusturmak.
# Sadece sayisal degiskenler icin yapmak istiyoruz;

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]      # Kategorik olmayan degiskenleri sectik; != 0 : esit degil, "O": Kategorikligi ifade etti (O: Object).
soz = {}                                                            # Bos bir sozluk olusturdum.
agg_list = ["mean", "min", "max", "sum"]                            # Yeni bir liste ekledim.

for col in num_cols:
    soz[col] = agg_list                                             # Value degelerine sabit liste ekledim.

# kisa yol;
new_dict = {col: agg_list for col in num_cols}                      # Key'ler degisiyor, sag taraftaki value'ler sabit.


# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}


df.head()

df[num_cols].head()                                                 # df[num_cols]: Kategorik degiskenlerden kurtulduk.

df[num_cols].agg(new_dict)                                          # "aggregation"a sozluk ekleyik dataframe'e uygularsak;
# Gonderdigimiz sozlugun icindeki dagiskenler df içerisinde varsa,
# bu degiskenleri key bolumunden tutar, value bolumune girdigimiz butun fonksiyonları gidip bu degiskenlere otomatik olarak uygular.
