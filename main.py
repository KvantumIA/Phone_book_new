# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

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
            Write_Contact()
            print('Контакт добавлен!')
        case 2:
            print('Просмотр контактов:')
            Print_contacts()
        case 3:
            print('Поиск контактов:')
            Find_contact()
        case 4:
            print('Изменение контакта')
            Edit_contacts()
        case 5:
            print('Удаление контакта')
            Delete_contacts()
        case 6:
            print('Выход')
            exit()
        case _:
            print('Такого пункта нет!')
    return num_action


def Write_Contact(telefon_list_name_file = 'Telephone_list.txt'):    #Записать новый контакт
    with open(telefon_list_name_file, 'a', encoding='UTF-8') as telefon_list:
        first_name = input("Введите фамилию: ")        
        last_name = input("Введите имя: ")
        telefon = input("Введите телефон: ")
        while len(telefon) != 11 or not telefon.isdigit():
            print('Вы ввели неправильный телефон')
            telefon = input("Введите телефон: ")
        telefon_list.write('\n' + last_name + ', ' +  first_name + ', ' +  telefon)


def Find_contact(telefon_list_name_file = 'Telephone_list.txt'):    #Поиск контактов
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        find_name = input('Поиск: ')
        lines = telefon_list.readlines()
        None_contact = True
        for i in lines:
            if find_name in i:
                print('Контакт найден:', i, end = '')
                None_contact = False
        if None_contact:
            print('Контакт не найден')


def Print_contacts(telefon_list_name_file = 'Telephone_list.txt'):  #Вывод всех контактов
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
        for i in lines:
            print(i, end = '')


def Edit_contacts(telefon_list_name_file = 'Telephone_list.txt'):  #Изменение контакта
    print('\n Фамилия | Имя | Телефон')
    with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list:
        telefon_list = telefon_list.read()
        print(telefon_list)
        print(' ')
        index_delete_data = int(input('Введите номер строки для редактирования: '))
        tel_book_lines = telefon_list.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(' , ')
        first_name = input("Введите фамилию: ") 
        last_name = input("Введите имя: ")      
        phone = input("Введите телефон: ")
        if len(first_name) == 0:
            first_name = elements[1]
            if len(last_name) == 0:
                last_name = elements[2]
                if len(phone) == 0:
                    phone = elements[2]
        edited_line = f'{first_name}, {last_name}, {phone}'
        tel_book_lines[index_delete_data] = edited_line
        print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
        with open(telefon_list_name_file, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))


def Delete_contacts(telefon_list_name_file = 'Telephone_list.txt'):    
    print('\n Имя | Фамилия | Телефон')
    with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list:
        telefon_list = telefon_list.read()
        print(telefon_list)
        print(' ')
        index_delete_data = int(input('Введите номер строки для удаления: ')) 
        tel_book_lines = telefon_list.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f'Удалена запись: {del_tel_book_lines}\n')
        with open(telefon_list_name_file, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))

print_menu()
enter_menu()