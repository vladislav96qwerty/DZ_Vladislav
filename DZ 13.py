n = int(input())
result = str(n)
while n > 9:
    res = 1
    for i in str(n):
        res = res * int(i)
    n = res
    result = result + " -> " + str(n)
result = result + " = " + str(n) + " Ответ: " + str(n)
print(result)