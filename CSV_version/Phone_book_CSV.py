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




Phone_book_file = "CSV_version\Telephone_list_2.csv"

# print_menu()
# enter_menu()







import customtkinter

class Interfeis(customtkinter.CTk):
    """Интерфейс программы"""
    def __init__(self):
        super().__init__()
        self.geometry("600x350")
        self.title("Телефонная книга")

        frame_button = customtkinter.CTkFrame(self, width= 200, height= 250, corner_radius= 0, bg_color="blue")
        frame_button.pack(padx = 20, pady = 20)
        frame_button.place(relx=0.2, rely=0.4, anchor=customtkinter.CENTER)

        self.button_Write_data = customtkinter.CTkButton(master = frame_button, text="Новый контакт", command=self.button_click_Write_data)
        self.button_Write_data.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.button_Print_contacts = customtkinter.CTkButton(master = frame_button, text="Вывод всех контактов", command=self.button_click_Print_contacts)
        self.button_Print_contacts.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.button_find_person = customtkinter.CTkButton(master = frame_button, text="Найти контакт", command=self.button_click_find_person)
        self.button_find_person.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.button_update_contact = customtkinter.CTkButton(master = frame_button, text="Изменить контакт", command=self.button_click_update_contact)
        self.button_update_contact.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.button_delete_contact = customtkinter.CTkButton(master = frame_button, text="Удалить контакт", command=self.button_click_delete_contact)
        self.button_delete_contact.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        frame_place = customtkinter.CTkFrame(self, width= 350, height= 250, corner_radius= 10, bg_color="blue")
        frame_place.pack(padx = 20, pady = 20)
        frame_place.place(relx=0.4, rely=0.4, anchor=customtkinter.W)

        # textbox = customtkinter.CTkTextbox(master=frame_place)
        # textbox.grid(row = len(Phone_book_file), column = 3)
        # textbox.insert("0.0", Print_contacts())

    def button_click_Write_data(self):
        print("Создан новый контакт")
    def button_click_Print_contacts(self):
        print("Вывод всех контактов")
    def button_click_find_person(self):
        print("Найти контакт")
    def button_click_update_contact(self):
        print("Изменить контакт")
    def button_click_delete_contact(self):
        print("Удалить контакт")

    

    # customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    # customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = Interfeis()
app.mainloop()