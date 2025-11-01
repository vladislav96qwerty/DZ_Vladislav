lists = [
    [2, 5, 10, 4, 6, 3],
    [9, 8, 7],
    [5],
    []
]
for numbers in lists:
    if len(numbers) == 0:
        result = 0
    else:
        sum_even_index = 0
        for i in range(0, len(numbers), 2):
            sum_even_index += numbers[i]
        result = sum_even_index * numbers[-1]
    print(result)