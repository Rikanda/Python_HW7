from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import controller



def open(dataset):
    window = Tk()
    window.title("Мой телефонный справочник")
    window.geometry('800x400')
    window.rowconfigure(index=0, weight=1)
    window.columnconfigure(index=0, weight=1)

    show_table(dataset)


# графические элементы для работы с записями справочника
    btn1 = ttk.Button(window, text ="Изменить выделенную запись",width=70, command=update_window)
    btn1.grid(column=0, row=2,sticky=E)
    btn2 = ttk.Button(window, text ="Дублировать выделенную запись",width=70, command=duplicate)
    btn2.grid(column=0, row=3,sticky=E)
    btn3 = ttk.Button(window, text ="Удалить выделенную запись",width=70, command=update)
    btn3.grid(column=0, row=4,sticky=E)
    btn4 = ttk.Button(window, text ="Обновить отображаемые записи",width=70, command=update)
    btn4.grid(column=0, row=5,sticky=E)
    btn5 = ttk.Button(window, text ="Удалить все записи",width=70, command=update)
    btn5.grid(column=0, row=6,sticky=E)
    btn6 = ttk.Button(window, text ="Добавить новую запись",width=70, command=update)
    btn6.grid(column=0, row=7,sticky=E)

# графические элементы для поиска записей в справочнике по фрагменту строки
    lbl_find = Label(window, text="Поиск записей по полю: ")
    lbl_find.grid(column=0, row=1,sticky=E)
    hdrs = ["Фамилия","Имя","Телефон"]
    hdrs_var = StringVar(value=hdrs[0])
    global combo1
    combo1 = ttk.Combobox(textvariable=hdrs_var, values=hdrs, state="readonly")
    combo1.grid(column=1,row=1)
    global entry
    entry = ttk.Entry()
    entry.grid(column=2,row=1)
    btn_find = ttk.Button(window, text ="Найти",width=10, command=find)
    btn_find.grid(column=3, row=1)

# графические элементы для выгрузки справочника в файл заданного формата
    lbl_exp = Label(window, text="Выбрать формат для выгрузки файла в текущий каталог: ")
    lbl_exp.grid(column=0, row=8, sticky=E)
    formats = ["csv","xml","json"]
    formats_var = StringVar(value=formats[0])
    combo2 = ttk.Combobox(textvariable=formats_var, values=formats, state="readonly")
    combo2.grid(column=1,row=8)
    selection_format = combo2.get()
    btn_exp = ttk.Button(window, text ="Выгрузить",width=10, command=update)
    btn_exp.grid(column=2, row=8)

# графические элементы для загрузки в справояник из файла
    lbl_imp = Label(window, text="Укажите путь и файл для загрузки данных в справочник: ")
    lbl_imp.grid(column=0, row=9, sticky=E)
    entry_imp = ttk.Entry()
    entry_imp.grid(column=1,row=9)
    btn_exp = ttk.Button(window, text ="Загрузить",width=10, command=update)
    btn_exp.grid(column=2, row=9)



    window.mainloop()

# заполнение таблицы
def show_table(dataset):
    global tree
    columns = ("id","surname","name","phone","description")
    tree = ttk.Treeview(columns=columns, show="headings")
    tree.grid(column=0,row=0, columnspan=3, sticky=NSEW)
    tree.heading("id", text = "№ записи", anchor=W)
    tree.heading("surname", text = "Фамилия", anchor=W)
    tree.heading("name", text = "Имя", anchor=W)
    tree.heading("phone", text = "Телефон", anchor=W)
    tree.heading("description", text = "Описание", anchor=W)

    tree.column("#1", stretch=NO, width=70)
    tree.column("#2", stretch=NO, width=100)
    tree.column("#3", stretch=NO, width=100)
    tree.column("#4", stretch=NO, width=100)
    tree.column("#5", stretch=NO, width=150)

    for d in dataset:
        tree.insert("", END, values=d)
    
    tree.bind("<<TreeviewSelect>>", item_selected)
    
    scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=3,sticky=NS)

# обновление записей
def update():
    data = controller.all_rows()
    show_table(data)


# поиск записей по условию
def find():
    selection_param = combo1.get()
    selection_text = entry.get()
    print(selection_param)
    print(selection_text)
    if selection_text:
        match selection_param:
            case "Фамилия":
                p = "surname"
            case "Имя":
                p = "name"
            case "Телефон":
                p = "phone"
        if p:
            data = controller.find_rows(p,selection_text)
            show_table(data)


# получение идентификатора выделенной записи
def item_selected(event):
    global id
    global datalist
    for selected_item in tree.selection():
        item = tree.item(selected_item)
    if item:
        datalist = item["values"]
        id = datalist[0]
        # print(id)

# дублирование записи
def duplicate():
    if tree.selection():
        controller.duplicat_row(id)
        update()

# окно изменения записи    
def update_window():
    if tree.selection():
        global u_window
        u_window = Tk()
        u_window.title("Изменить")
        u_window.geometry("250x200")

        global entry_surname
        global entry_name
        global entry_phone
        global entry_description

        lbl_surname = Label(u_window, text="Фамилия *: ")
        lbl_surname.grid(column=0, row=0,sticky=E)
        entry_surname = Entry(u_window)
        entry_surname.grid(column=1,row=0)
        entry_surname.insert(0,datalist[1])

        lbl_name = Label(u_window, text="Имя *: ")
        lbl_name.grid(column=0, row=1,sticky=E)
        entry_name = Entry(u_window)
        entry_name.grid(column=1,row=1)
        entry_name.insert(0,datalist[2])

        lbl_phone = Label(u_window, text="Телефон *: ")
        lbl_phone.grid(column=0, row=2,sticky=E)
        entry_phone = Entry(u_window)
        entry_phone.grid(column=1,row=2)
        entry_phone.insert(0,datalist[3])

        lbl_description = Label(u_window, text="Описание: ")
        lbl_description.grid(column=0, row=3,sticky=E)
        entry_description = Entry(u_window)
        entry_description.grid(column=1,row=3)
        entry_description.insert(0,datalist[4])

        accept = Button(u_window, text ="Сохранить",width=10, command=save)
        accept.grid(column=1, row=4)

# сохранение изменений  
def save():
    if entry_surname == 0 or entry_name == 0 or entry_phone == 0:
        showerror("Error", message= "Не заполнено обязательное поле!")
    else:
        str_data = (entry_surname.get(),entry_name.get(),entry_phone.get(),entry_description.get(),id)
        controller.update_row(str_data)
        update()
        u_window.destroy()
        
