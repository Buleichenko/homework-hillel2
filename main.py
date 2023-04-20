a = float(input("Длина стороны а: "))
b = float(input("Длина стороны b: "))
c = float(input("Длина стороны с: "))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))
print("Площадь треугольника равна:", s)
