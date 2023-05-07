password = input("Ведите пароль: ")
score = 0

if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char in '+-/_%$#@;*&^:?><}{[]!' for char in password):
    score += 1

print(f"Количество балов за пароль: {score}")

if score == 0:
    print("Используйте заглавные буквы")
    print("Минимальная длина пароля 8")
    print("Использовать цифры")
    print("Использовать специальные символы")
elif score < 5:
    if not any(char.isupper() for char in password):
        print("Используйте заглавные буквы")
    if len(password) < 8:
        print("Минимальная длина пароля 8")
    if not any(char.isdigit() for char in password):
        print("Использовать цифры")
    if not any(char in ['+', '-', '/', '_', '%', '@', '$', '*', '&', '<', '>', '{', '}'] for char in password):
        print("Используйте специальные символы")
else:
    print("Пароль сложный и надежный!")

