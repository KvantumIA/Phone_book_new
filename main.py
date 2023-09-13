# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def Interfeis_contact(telefon_list_name_file = 'Telephone_list.txt'):
    interfeis_contact = int(input('Введите 1 для поиска, введите 2 для добавления контакта, 3 для вывода всех контактов, 4 для изменения контакта, 5 для удаления контакта, 0 для выхода: '))
    while interfeis_contact != 0:
        if interfeis_contact == 1:
            Find_contact()
        elif interfeis_contact == 2:
            Write_Contact()
        elif interfeis_contact == 3:
            Print_contacts()
        elif interfeis_contact == 4:
            Edit_contacts()
        elif interfeis_contact == 5:
            Delete_contacts()  
        interfeis_contact = int(input('\n Введите 1 для поиска, введите 2 для добавления контакта, 3 для вывода всех контактов, 4 для изменения контакта, 5 для удаления контакта, 0 для выхода: '))


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


Interfeis_contact()


# import customtkinter

# сlass ButtonClass:

#     def button_Write_Contact():
#         print(Write_Contact(telefon_list_name_file = "Telefon_list.txt"))


# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()
# app.title("Телефонная книга")
# app.geometry("400x300")

# # Use CTkButton instead of tkinter Button
# button_Write_Contact = customtkinter.CTkButton(master=app, text="Новый контакт", command=button_Write_Contact)
# button_Write_Contact.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)


# app.mainloop()