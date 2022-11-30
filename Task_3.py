# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def list_completion(my_list: list, length: int):
    for i in range(0, length):
        my_list.append(round(random.uniform(1, 10), 2))
    # print(my_list)
    return my_list


def subtraction_max_min(my_list: list):
    for i in range(0, len(my_list)):
        my_list[i] = (round(my_list[i] - int(my_list[i]), 2))
    subtraction = round(max(my_list) - min(my_list), 2)
    return subtraction


first_list = []
list_length = random.randint(4, 6)
first_list = list_completion(first_list, list_length)
print(f'{first_list} => {subtraction_max_min(first_list)}')
