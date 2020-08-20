from tkinter import *

window = Tk()
window.title("PhoneBook")
window.geometry("400x200")

label_tel = Label(text = "Номер телефона")
input_tel = Entry()

label_last_name = Label(text = "Фамилия")
input_last_name = Entry()

label_first_name = Label(text = "Имя")
input_first_name = Entry()

label_patronimyc = Label(text = "Отчество")
input_patronimyc = Entry()

label_address = Label(text = "Адрес")
input_address = Entry()

label_tel.grid(row=0, column=0, padx=10, pady=4)
input_tel.grid(row=0, column=1)

label_last_name.grid(row=1, column=0, padx=10, pady=4)
input_last_name.grid(row=1, column=1)

label_first_name.grid(row=2, column=0, padx=10, pady=4)
input_first_name.grid(row=2, column=1)

label_patronimyc.grid(row=3, column=0, padx=10, pady=4)
input_patronimyc.grid(row=3, column=1)

label_address.grid(row=4, column=0, padx=10, pady=4)
input_address.grid(row=4, column=1)

window.mainloop()

