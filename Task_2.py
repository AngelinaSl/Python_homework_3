# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def list_completion(my_list: list, length: int):
    for i in range(0, length):
        my_list.append(random.randint(1, 10))
    # print(my_list)
    return my_list


def search_sum(my_list: list):
    new_list = []
    index_pos = 0
    index_neg = -1
    while index_pos < len(my_list) / 2:
        sum_number = 0
        sum_number = my_list[index_pos] + my_list[index_neg]
        new_list.append(sum_number)
        index_pos += 1
        index_neg -= 1
    return new_list


first_list = []
list_length = random.randint(4, 6)
x = list_completion(first_list, list_length)
print(f"{x} => {search_sum(x)}")
