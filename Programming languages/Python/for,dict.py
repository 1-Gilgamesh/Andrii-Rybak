#подвоєння літер
a = "Maserati"
b = ""
for i in a:
    b += i*2
print (str(b), "\n")

#обернене виконання команди ===========================
a = "live"
b = ""
for i in a[::-1]:
    b += i
print (str(b), "\n")

#Паліндроми ==================================
import random
list = []
palindromes = []

for i in range(201):
    ran_num = random.randint(11, 1002)
    list.append(ran_num)

for i in list:
    str1 = (str(i))
    if str1 == str1[::-1]:
        pal = (int(str1))
        palindromes.append(pal)

count_pal=len(palindromes)
print("Amount of palindromes: ",count_pal,"\nnamely: ",palindromes, "\n")

#Приклад наслідування ========================
footballer1 = {'Name': 'Andrii', 'surname': 'Shevchenko', 'Age': 38, 'Height': 1.81}
goalkeeper = footballer1.copy()
goalkeeper["lenth of arms"] = 0.73
print(goalkeeper)