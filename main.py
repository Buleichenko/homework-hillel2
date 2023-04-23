a = float(input("Длина стороны a: "))
b = float(input("Длина стороны b: "))
c = float(input("Длина стороны c: "))

p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Площадь треугольника равна", s)
