# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 48 -> 110000
# - 3 -> 11
# - 2 -> 10


def find_binary_number(x: int):
    y = ''
    while x > 0:
        y = str(x % 2) + y
        x = x//2
    print(y)


number = int(input('Введите число: '))
find_binary_number(number)
