print('Hello Teacher')
number = int(input("Введіть 5-значне число: "))
a1 = number // 10000
a2 = (number // 1000) % 10
a3 = (number // 100) % 10
a4 = (number // 10) % 10
a5= number % 10
number = a5 * 10000 + a4 * 1000 + a3 * 100 + a2 * 10 + a1
print(number)
