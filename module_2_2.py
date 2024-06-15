# Все ли равны?

# Ввод целых чисел + математическое округление до целого, если пользователь ввел число с плав.точкой
first = int(round(float(input('Введите первое число: '))))
second = int(round(float(input('Введите второе число: '))))
third = int(round(float(input('Введите третье число: '))))

# Сравнение переменных и вывод
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
