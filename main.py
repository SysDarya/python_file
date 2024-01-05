from functions import add_contacts, print_contacts, find_contacts, change_contacts

file_name = './contacts.txt'


def draw_interface():
    print("""
     1 - Просмотреть список контактов
     2 - Добавить контакт
     3 - Найти контакт
     4 - Изменить контакт
     5 - Удалить контакт
     6 - Выход из программы
    """)

def main():
    run = True
    while run:
        draw_interface()
        option = input('Ваш выбор: ')
        if not option.isnumeric():
            print('\n!!!Введите корректный номер опции!!!\n'.upper())
        else:
            match int(option):
                case 1:
                    print_contacts(file_name)
                case 2:
                    add_contacts(file_name)
                case 3:
                    find_contacts(file_name)
                case 4:
                    change_contacts(file_name)
                case 5:
                    change_contacts(file_name, False)
                case 6:
                    print('конец работы'.upper())
                    run = False
                case _:
                    print('Такой опции не существует')



if __name__ == '__main__':
    main()