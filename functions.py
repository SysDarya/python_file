def get_user_data(msg):
    user_data = input(msg + ': ')
    return user_data


def pretty_print(data):
    print('-' * 10 + '\n')
    print(*data, sep='\n')
    print('\n' + '-' * 10)


def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        data = file.readlines()
        pretty_print(data)


def add_contacts(file_name):
    data = get_user_data('Введите ФИО и номер (Пример: Иванов Иван Иванович 89165122452)')
    with open(file_name, 'a', encoding='utf8') as file:
        file.write('\n' + data)
        print('Контакт добавлен')


def find_contacts(file_name, flag=None):
    data = get_user_data(f'Напишите данные пользователя, которого вы хотите {"изменить" if flag == 2 else "удалить" if flag else "найти" } - Имя, Фамилию или номер')
    with open(file_name, 'r', encoding='utf8') as file:
        filter_list = []
        lines = file.readlines()
        for line in lines:
            if data.capitalize() in line:
                filter_list.append(line.strip('\n'))

        pretty_print(filter_list)
        if flag == 1:
            return filter_list[0]
        return filter_list




def change_contacts(file_name, flag=True):
    contact = find_contacts(file_name, flag=(2 if flag else 1))
    with open(file_name, 'r', encoding='utf8') as file:
        lines = file.readlines()
    with open(file_name, 'w', encoding='utf8') as file:
        for line in lines:
            if flag:
                if line.strip('\n') == contact[0]:
                    new_user = get_user_data('Введите новые данные (Пример: Иванов Иван Иванович 89165122452)')
                    file.write(new_user + '\n')
                else:
                    file.write(line)
            else:
                if line.strip('\n') != contact:
                    file.write(line)




