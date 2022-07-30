### PART1 : Data Structures
x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
c
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"python", "Machine Learning", "Data Science"}
type(s)


# shortcut;
R = [8, 3.2, 8j + 18, "Hello Rumeysa",
     True, 23 < 12, [1, 2, 3, 4, 5],
     {"Name" : "Hello World", "Age" : 27, "Address" : "Downtown"},
     ("Machine Learning", "Data Science"),
     {"python", "Machine Learning", "Data Science"}]
for i in R:
  print(type(i))



### PART2 : Convert all letters of the given string to uppercase. Put space instead of commas and periods, separate them word by word.
# (Verilen string ifadenin tum harflerini buyuk harfe ceviriniz. Virgul ve nokta yerine space koyunuz, kelime kelime ayiriniz.)

string = "The goal is to turn data into information, and information into insight."
string.upper()
string_new = string.upper()
string_new2 = string_new.replace(",", " ")
string_new3 = string_new.replace(".", " ")
string_end = string_new3.split()

print(string_end)


# shortcut;
string = "The goal is to turn data into information, and information into insight."
string_new = string.replace(".", " ").replace(",", " ").upper().split()
print(string_new)



### PART3 : Making changes to the list;

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Access the number of elements;
len(lst)

# Accessing the 0th and 10th indexes;
lst[0], lst[10]

# Creating a list from a list;
list = lst[:4]
print(list)

# Deleting element at specific index;
del lst[2]
print(lst)

# Adding a new element;
lst.append("N")
print(lst)

# Adding an element to a specific index;
lst.insert(8, "N")
print(lst)

len(lst)



### PART4 : Change in dictionary structure;

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# Accessing key values;
dict.keys()

# Accessing values;
dict.values()

# Changing the key value;
dict.update({"Daisy": ["England", 13]})
print(dict)

# Adding to the dictionary;
dict["Ahmet"] = "Turkey", 24
print(dict)

# Delete from dictionary;
dict.pop("Antonio")
print(dict)



### PART5 : Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns these lists;
# Arguman olarak bir liste alan, listenin icerisindeki tek ve cift sayilari ayri listelere atayan ve bu listeleri return eden fonksiyon yaziniz.

l = [2, 13, 18, 93, 22]


def func(list):
    even_list = []
    odd_list = []
    [even_list.append(i) if i % 2 == 0 else odd_list.append(i) for i in list]
    return even_list, odd_list


even_list, odd_list = func(l)


# Other way;
l = [2, 13, 18, 93, 22]
even_list = [i for i in l if i % 2 == 0]
odd_list = [i for i in l if i % 2 != 0 ]

even_list, odd_list = func(l)
print(func(l))



### PART6 : Using the "List Comprehension" structure, capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning of the names;
# List Comprehension yapisi kullanarak car_crashes verisindeki numeric degiskenlerin isimlerini buyuk harfe ceviriniz ve basina NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM_" + i.upper() if df[i].dtype != "O" else i.upper() for i in df.columns]
print(df.columns)



### PART7 : Using the "List Comprehension" structure, writing "FLAG" after the names of the variables that do not contain "no" in their names in the car_crashes data;
# List Comprehension yapisi kullanarak car_crashes verisinde isminde "no" barindirmayan degiskenlerin isimlerinin sonuna "FLAG" yaziniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [i.upper() + "_FLAG" if "no" not in i else i.upper() for i in df.columns]
print(df.columns)



### PART8 : Using the "List Comprehension" structure, choosing the names of the variables that are DIFFERENT from the given variable names and creating a new data frame;
# List Comprehension yapisi kullanarak verilen (og_list = ["abbrev", "no_previous"]) degisken isimlerinden FARKLI olan degiskenlerin isimlerini seciniz ve yeni bir dataframe olusturunuz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]

new_cols = [i for i in df.columns if i not in og_list]

new_df = df[new_cols]
new_df.head()