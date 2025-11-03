while True:
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
        if b == 0:
            print("Помилка: не можна ділити на нуль!")
        else:
            result = a / b
            print("Результат:", result)
    else:
        print("Помилка: невідома дія!")
    again = input("Бажаєте продовжити? (y/yes для продовження): ").lower()
    if again not in ("y", "yes"):
        print("Роботу калькулятора завершено.")
        break