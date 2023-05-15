# Завдання 1
numbers = []

for i in range(5):
    num = int(input("Введіть число: "))
    numbers.append(num)

print("Список чисел: ", numbers)

# Завдання 2
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

# Завдання 3
A = []

for i in range(10):
    num = int(input("Введіть число: "))
    A.append(num)

N = int(input("Введіть число, яке шукаєте: "))
count = 0

for num in A:
    if num == N:
        count += 1

print("Кількість повторень числа {}: {}".format(N, count))

# Завдання 4
A = []
N = int(input("Введіть кількість чисел: "))

for i in range(N):
    num = int(input("Введіть число: "))
    A.append(num)

print("Список чисел у зворотній послідовності: ", A[::-1])

# Завдання 5
A = []
C = []

for i in range(5):
    num = int(input(f"Введіть число {i+1}: "))
    A.append(num)

for num in A:
    if num > 5:
        C.append(num)

print("Числа, що більші за 5:", C)

# Завдання 6
A = []
n = int(input("Введіть кількість чисел: "))

for i in range(n):
    num = int(input(f"Введіть число {i+1}: "))
    A.append(num)

min_num = A[0]
max_num = A[-1]
for num in A:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Мінімальне значення:", min_num)
print("Максимальне значення:", max_num)

# Завдання 7
import re

text = input("Введіть текст: ")

digits = re.findall(r'\d', text)

print("Кількість цифр: ", len(digits))


