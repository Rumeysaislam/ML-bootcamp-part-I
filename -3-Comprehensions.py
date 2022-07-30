# COMPREHENSIONS

### List Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]

# Foksiyonumuz;
def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))


# Uzun uzun yazmak yerine, "Comprehension" kullaniriz;
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]


[salary * 2 for salary in salaries if salary < 3000]                    # Sadece if varsa "for salary in salaries" sola yazilir.

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]    # if ile else birlikte kullanılmıs ise "for salary in salaries" saga yazilir.

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]



# Baska bir ornek yapalim;
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]


# "not in" kullanımı;
[student.upper() if student not in students_no else student.lower() for student in students]




### Dict Comprehension

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

# key'lere dokunmadan valuelerin karesini almak istiyoruz; (k, v): indexlerimiz

{k: v ** 2 for (k, v) in dictionary.items()}

# key"lere islem yapmak (v sabit) istersem;
{k.upper(): v for (k, v) in dictionary.items()}

# key'lere de value'lere de islem yapmak istersem;
{k.upper(): v*2 for (k, v) in dictionary.items()}




### Uygulama

# Amaç: Cift sayilarin karesi alinarak bir sozluge eklemek;

# Key'ler orijinal degerler value'lar ise degistirilmis degerler olacak.


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:                                                      # n :cift sayilar
        new_dict[n] = n ** 2                                            # Koseli parantez icerisinde yazinca otomatik keylere atiyor!
new_dict

# Uzun uzun yazmak yerine, "Comprehension" kullaniriz;
numbers = range(10)
new_dict = {}

{n: n ** 2 for n in numbers if n % 2 == 0}