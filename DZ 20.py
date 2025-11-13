def add_one(some_list):
    num = 0
    for digit in some_list:
        num = num * 10 + digit
    num += 1
    result = []
    while num > 0:
        result.insert(0, num % 10)
        num //= 10
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
