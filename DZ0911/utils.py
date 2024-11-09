import re

def get_reg_data():
    # Определяем паттерны для проверки
    patterns = {
        'name': r'^[A-Za-zА-Яа-яЁё\s]+$',  # Имя: только буквы и пробелы
        'email': r'^[\w\.-]+@[\w\.-]+\.\w+$',  # Email: стандартный формат
        'phone': r'^\+?\d{10,15}$'  # Телефон: от 10 до 15 цифр с возможным знаком +
    }
    return patterns

def check_unique_data(user_data, data_to_check):
    # Проверяем уникальность данных
    return user_data not in data_to_check

def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    # Проверяем введенные данные по паттерну
    if re.match(reg_pattern, user_data):
        if data_to_check:
            if check_unique_data(user_data, data_to_check):
                return user_data
            else:
                print("Ошибка: Данные не уникальны.")
                return None
        return user_data
    else:
        print("Ошибка: Данные не соответствуют паттерну.")
        return None
