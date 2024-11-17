def print_info(*args, **kwargs):
    # Печатаем позиционные аргументы
    print("Позиционные аргументы:")
    for arg in args:
        print(arg)

    # Печатаем именованные аргументы
    print("\nИменованные аргументы:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Пример вызова функции
print_info(1, 2, 3, name="Alice", age=30, city="Moscow")
