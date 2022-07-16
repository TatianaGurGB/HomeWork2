# Реализуйте алгоритм перемешивания списка.

from re import A


my_list = [4, 2, 5, 6, 7, 3, 1]
size = len(my_list)
i = 0
print(my_list)

while size > len(my_list) / 2:
    my_list[i], my_list[size - 1] = my_list[size - 1], my_list[i]
    i += 1
    size -= 1
print(my_list)

