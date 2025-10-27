a = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

if operation == '+':
    result = a + b
    print("Результат:", result)
elif operation == '-':
    result = a - b
    print("Результат:", result)
elif operation == '*':
    result = a * b
    print("Результат:", result)
elif operation == '/':
    if b == 0:  # Перевіряємо дільник (b), а не ділене (a)
        print("Помилка: не можна ділити на нуль!")
    else:
        result = a / b
        print("Результат:", result)
else:
    print("Помилка: невідома дія!")