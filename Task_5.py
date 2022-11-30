# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def negafibonacci(my_list: list):
    new_list = []
    i = len(my_list)
    while 0 < i:
        if i % 2 == 0:
            new_list.append((-my_list[i - 1]))
        else:
            new_list.append((my_list[i - 1]))
        i -= 1
    new_list.append(0)
    i = 0
    for i in range(0, len(my_list)):
        new_list.append(my_list[i])
    return new_list


number = int(input('Введите число: '))
fib_list = []
for e in range(1, number + 1):
    fib_list.append(fib(e))
print(f'k = {number}, Негафибоначчи: {negafibonacci(fib_list)}')
