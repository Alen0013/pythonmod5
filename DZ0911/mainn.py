from utils import get_reg_data, reg_check


def main():
    users_list = []
    patterns = get_reg_data()

    while len(users_list) < 3:
        user_data = []
        for field in ['name', 'email', 'phone']:
            while len(user_data) < 4:
                data = input(f"Введите {field}: ")
                if field == 'phone':
                    data_to_check = [user[2] for user in users_list]
                elif field == 'email':
                    data_to_check = [user[1] for user in users_list]
                else:
                    data_to_check = None
                result = reg_check(data, patterns[field], users_list, data_to_check)
                if result is not None:
                    user_data.append(result)
                    break

        if len(user_data) == 3:
            users_list.append(user_data)
            print("Пользователь добавлен:", user_data)
        else:
            print("Ошибка: Не удалось добавить пользователя.")

if __name__ == "__main__":
    main()
