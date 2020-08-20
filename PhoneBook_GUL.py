from tkinter import *

phone_book=dict()

def clear():
    input_tel.delete(0,END)
    input_last_name.delete(0,END)
    input_first_name.delete(0,END)
    input_patronimyc.delete(0,END)
    input_address.delete(0,END)


def add():
    value = list()
    value.append(input_last_name.get())
    value.append(input_first_name.get())
    value.append(input_patronimyc.get())
    value.append(input_address.get())
    phone_book[input_tel.get()] = value



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

button_add= Button(text="Добавить", command=add)
button_clear= Button(text="Очистить", command=clear)

label_tel.grid(row=0, column=0, padx=10, pady=4, sticky="w")
input_tel.grid(row=0, column=1)

label_last_name.grid(row=1, column=0, padx=10, pady=4, sticky="w")
input_last_name.grid(row=1, column=1, padx=10)

label_first_name.grid(row=2, column=0, padx=10, pady=4, sticky="w")
input_first_name.grid(row=2, column=1)

label_patronimyc.grid(row=3, column=0, padx=10, pady=4, sticky="w")
input_patronimyc.grid(row=3, column=1, padx=10)

label_address.grid(row=4, column=0, padx=10, pady=4, sticky="w")
input_address.grid(row=4, column=1)

button_add.grid(row=1, column=2)
button_clear.grid(row=3, column=2)

window.mainloop()

