my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) == 0:
    result = [[], []]
else:
    middle = len(my_list) // 2
    if len(my_list) % 2 == 1:
        middle = middle + 1
    first_part = my_list[:middle]
    second_part = my_list[middle:]
    result = [first_part, second_part]
print(result)
