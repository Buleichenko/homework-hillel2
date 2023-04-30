n = int(input("Введите число N: "))
i = 0
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1

n = int(input("Введите число N: "))
i = 0
summa = 0
while i <= n:
    if i % 3 == 0:
        summa += i
    i += 1
print("Числа от 0 до N, которые делятся на 3 без остатка: ", summa)
