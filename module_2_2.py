first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and second == third:
    print('Три')
elif first == second or second == third or first == third:
    print('Два')
else:
    print('Ноль')
