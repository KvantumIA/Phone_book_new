import os

def print_menu():
    print('\nВыберите пункт меню:')
    print('1.Добавить контакт')
    print('2.Посмотреть контакты')
    print('3.Поиск контакта')
    print('4.Изменение контакта')
    print('5.Удаление контакта')

    print('\n6.Выход')


def enter_menu():
    num_action = int(input('\n\nВведите пункт меню: '))
    os.system('cls')
    match num_action:
        case 1:
            print('Добавление контакта:')
            write_data()
            print('Контакт добавлен!')
        case 2:
            print('Просмотр контактов:')
            # Print_contacts()
        case 3:
            print('Поиск контактов:')
            find_person()
        case 4:
            print('Изменение контакта')
            update_contact()
        case 5:
            print('Удаление контакта')
            delete_contact()
        case 6:
            print('Выход')
            exit()
        case _:
            print('Такого пункта нет!')
    return num_action

def write_person(second_name, first_name, phone):
    with open('directory.txt', 'a', encoding='UTF-8') as f:
        f.write(f'\n{second_name}, {first_name}, {phone}')

def write_data():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    write_person(second_name, first_name, phone)

def find_person():
    find_name = input('Поиск контакта: ')
    data = open('directory.txt', 'r', encoding='UTF-8')
    None_contact = True
    for i in data.readlines():
        if find_name in i:
            print('Контакт найден:', i, end = '')
            None_contact = False
    if None_contact:
        print('Контакт не найден')
    data.close()

def update_contact():
    search_name = input('Введите фамилию контакта, который хотите изменить: ')
    with open("directory.txt", "r", encoding='UTF-8') as f:
        lines = f.readlines()
    with open("directory.txt", "r+", encoding='UTF-8') as f:
        None_contact = True
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.lower() in contact[0].lower():
                new_second_name = input('Введите новую фамилию: ')
                new_first_name = input('Введите новое имя: ')
                new_phone = input('Введите новый номер телефона: ')
                f.write(line)
                f.write(f'{new_second_name}, {new_first_name}, {new_phone}')
                print('Контакт успешно изменен!')                        
                None_contact = False
        if None_contact:
            print('Контакт не найден')

def delete_contact():
    search_name = input('Введите фамилию контакта, который хотите удалить: ')
    with open("directory.txt", "r", encoding='UTF-8') as f:
        lines = f.readlines()
    with open("directory.txt", "w", encoding='UTF-8') as f:
        contact_found = False
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.lower() not in contact[0].lower():
                f.write(line)
            else:
                contact_found = True
        if contact_found:
            print('Контакт успешно удален!')
        else:
            print('Контакт не найден.')



path = 'directory.txt'
print_menu()
enter_menu()