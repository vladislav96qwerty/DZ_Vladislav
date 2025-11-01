lists = [
    [0, 8, 0, 24, 5],
    [0],
    [9, 0, 66, 0, 0, 0, 5],
    [4, 0, 6, 31, 0, 55, 0, 47, 0, 45, 0, 0, 86, 0]
]
for first_list in lists:
    new_list = []
    for n in first_list:
        if n != 0:
            new_list.append(n)
    zero_count = first_list.count(0)
    for i in range(zero_count):
        new_list.append(0)
    print(new_list)