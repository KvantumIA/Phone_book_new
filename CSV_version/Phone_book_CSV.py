import os
import csv

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
            Write_data()
            print('Контакт добавлен!')
        case 2:
            print('Просмотр контактов:')
            Print_contacts()
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


def Write_data():
    first_name = input('Введите фамилию: ')
    second_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    new_contact = {"first_name": first_name, "last_name": second_name, "phone": phone}
    with open(Phone_book_file, 'a', newline="", encoding='UTF-8') as file:
        columns = ["first_name", "last_name", "phone"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(new_contact)

def Print_contacts():
    with open(Phone_book_file, 'r', newline="", encoding='UTF-8') as file:
        writer = csv.DictReader(file)
        for row in writer:
            print("Фамилия:", row["first_name"], ",", "Имя:", row["last_name"], ",", "Номер телефона:", row["phone"])

def find_person():
    find_name = input('Поиск контакта: ')
    with open(Phone_book_file, 'r', encoding='UTF-8') as file:
        writer = csv.DictReader(file)
        None_contact = True
        for row in writer:
            if row["first_name"].lower() == find_name.lower():
                print("Фамилия:", row["first_name"], ",", "Имя:", row["last_name"], ",", "Номер телефона:", row["phone"])
                None_contact = False
            elif row["last_name"].lower() == find_name.lower():
                print("Фамилия:", row["first_name"], ",", "Имя:", row["last_name"], ",", "Номер телефона:", row["phone"])
                None_contact = False
            elif row["phone"] == find_name.lower():
                print("Фамилия:", row["first_name"], ",", "Имя:", row["last_name"], ",", "Номер телефона:", row["phone"])
                None_contact = False
        if None_contact:
            print('Контакт не найден')

def Correct_contact(row):
    first_name = input('Введите измененную фамилию: ')
    second_name = input('Введите изменненое имя: ')
    phone = input('Введите новый номер телефона: ')
    new_contact = {"first_name": first_name, "last_name": second_name, "phone": phone}
    with open(Phone_book_file, 'r+', encoding='UTF-8') as file:
        columns = ["first_name", "last_name", "phone"]
        writer = csv.DictWriter(file, fieldnames=columns)
        row["first_name"] = first_name
        row["second_name"] = second_name
        row["phone"] = phone

def update_contact():
    search_name = input('Введите фамилию контакта, который хотите изменить: ')
    temp_file = "temp_directory.csv"
    with open(Phone_book_file, 'r', encoding='UTF-8') as input_file, \
            open(temp_file, 'w', newline='', encoding='UTF-8') as output_file:
        columns = ["first_name", "last_name", "phone"]
        reader = csv.DictReader(input_file, fieldnames=columns)
        writer = csv.DictWriter(output_file, fieldnames=columns)
        None_contact = True
        for row in reader:
            if row["first_name"].lower() == search_name.lower() or \
               row["last_name"].lower() == search_name.lower() or \
               row["phone"].lower() == search_name.lower():
                new_second_name = input('Введите новую фамилию: ')
                new_first_name = input('Введите новое имя: ')
                new_phone = input('Введите новый номер телефона: ')
                row["first_name"] = new_first_name      # Вносим изменения в запись
                row["last_name"] = new_second_name
                row["phone"] = new_phone
                
                print('Контакт успешно изменен!')
                None_contact = False
            writer.writerow(row)
    os.remove(Phone_book_file)
    os.rename(temp_file, Phone_book_file)
    if None_contact:
        print('Контакт не найден')


def delete_contact():
    search_name = input('Введите фамилию контакта, который хотите удалить: ')
    temp_file = "temp_directory.csv"
    with open(Phone_book_file, 'r', encoding='UTF-8') as input_file, \
            open(temp_file, 'w', newline='', encoding='UTF-8') as output_file:
        columns = ["first_name", "last_name", "phone"]
        reader = csv.DictReader(input_file, fieldnames=columns)
        writer = csv.DictWriter(output_file, fieldnames=columns)
        None_contact = True
        for row in reader:
            if row["first_name"].lower() == search_name.lower() or \
               row["last_name"].lower() == search_name.lower() or \
               row["phone"].lower() == search_name.lower():
                print('Контакт успешно удален!')
                None_contact = False
            else:
                writer.writerow(row)
    os.remove(Phone_book_file)
    os.rename(temp_file, Phone_book_file)
    if None_contact:
        print('Контакт не найден')




Phone_book_file = "Telephone_list_2.csv"

print_menu()
enter_menu()