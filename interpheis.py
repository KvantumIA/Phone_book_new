import customtkinter


сlass ButtonClass:

    @staticmethod
    def button_Write_Contact():
        print(Write_Contact(telefon_list_name_file = "Telefon_list.txt"))


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("Телефонная книга")
app.geometry("400x300")

# Use CTkButton instead of tkinter Button
button_Write_Contact = customtkinter.CTkButton(master=app, text="Новый контакт", command=button_Write_Contact)
button_Write_Contact.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)


app.mainloop()