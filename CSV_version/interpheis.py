import customtkinter

class Interfeis:
    """Интерфейс программы"""
    def __init__(self, Phone_book_file):
        self.Phone_book_file = Phone_book_file

    def button_Write_Contact(self):
        print("Button1")



Phone_book_file = "CSV_version/Telephone_list_2.csv"

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("Телефонная книга")
app.geometry("400x300")

# Use CTkButton instead of tkinter Button
button_Write_Contact = customtkinter.CTkButton(master=app, text="Новый контакт", command=self)
button_Write_Contact.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)


app.mainloop()