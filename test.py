def Interfeis_contact(telefon_list_name_file = 'Telefon_list.txt'):
    interfeis_contact = int(input('Введите 1 для поиска, введите 2 для добавления контакта, 3 для удаления контакта, 4 для редактирования, 5 для вывода всех контактов, 0 для выхода: '))
    while interfeis_contact != 0:
        if interfeis_contact == 1:
            Find_contact()
        elif interfeis_contact == 2:
            Write_Contact()
        elif interfeis_contact == 3:
            Delete_contacts()
        elif interfeis_contact == 4:
            Edit_contacts()
        else:
            Print_contacts()
        interfeis_contact = int(input('\n Введите 1 для поиска, введите 2 для добавления контакта, 3 для удаления контакта, 4 для редактирования, 5 для вывода всех контактов, 0 для выхода: '))


def Write_Contact(telefon_list_name_file = 'Telefon_list.txt'):
    with open(telefon_list_name_file, 'a', encoding='UTF-8') as telefon_list:
        first_name = input("Введите фамилию: ")        
        last_name = input("Введите имя: ")
        telefon = input("Введите телефон: ")
        while len(telefon) != 11 or not telefon.isdigit():
            print('Вы ввели неправильный телефон')
            telefon = input("Введите телефон: ")
        telefon_list.write('\n' + last_name + ', ' +  first_name + ', ' +  telefon)


def Find_contact(telefon_list_name_file = 'Telefon_list.txt'):
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


def Print_contacts(telefon_list_name_file = 'Telefon_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
        for i in lines:
            print(i, end = '')


def Delete_contacts(telefon_list_name_file = 'Telefon_list.txt'):
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


def Edit_contacts(telefon_list_name_file = 'Telefon_list.txt'):
    print('\n Имя | Фамилия | Телефон')
    with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list:
        telefon_list = telefon_list.read()
        print(telefon_list)
        print(' ')
        index_delete_data = int(input('Введите номер строки для редактирования: '))
        tel_book_lines = telefon_list.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(' , ')
        last_name = input("Введите имя: ")
        first_name = input("Введите фамилию: ")        
        phone = input("Введите телефон: ")
        if len(first_name) == 0:
            first_name = elements[1]
            if len(last_name) == 0:
                last_name = elements[2]
                if len(phone) == 0:
                    phone = elements[2]
        edited_line = f'{last_name}, {first_name}, {phone}'
        tel_book_lines[index_delete_data] = edited_line
        print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
        with open(telefon_list_name_file, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))

Interfeis_contact()