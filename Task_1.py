# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной индексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных индексах элементы 3 и 9, ответ: 12


def list_completion_sum_calculation(my_list: None):
    if my_list is None:
        my_list = []
    sum_numbers = 0
    for i in range(0, 5):
        my_list.append(random.randint(1, 10))
        if i % 2 == 1:
            sum_numbers += my_list[i]

    print(my_list)
    print(f"Сумма элементов на нечетных индексах = {sum_numbers}")


empty_list = None
list_completion_sum_calculation(empty_list)