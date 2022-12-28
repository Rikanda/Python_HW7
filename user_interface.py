from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter import filedialog
import controller



def open():
    window = Tk()
    window.title("Мой телефонный справочник")
    window.geometry('800x400')
    window.rowconfigure(index=0, weight=1)
    window.columnconfigure(index=0, weight=1)

# при открытии всегда обновляем таблицу с записями справочника из БД
    update()


# графические элементы для поиска записей в справочнике по фрагменту строки (с учетом регистра)
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

# графические элементы для работы с записями справочника
    btn1 = ttk.Button(window, text ="Изменить выделенную запись",width=70, command=update_window)
    btn1.grid(column=0, row=2,sticky=E)
    btn2 = ttk.Button(window, text ="Дублировать выделенную запись",width=70, command=duplicate)
    btn2.grid(column=0, row=3,sticky=E)
    btn3 = ttk.Button(window, text ="Удалить выделенную запись",width=70, command=delete_row)
    btn3.grid(column=0, row=4,sticky=E)
    btn4 = ttk.Button(window, text ="Обновить отображаемые записи",width=70, command=update)
    btn4.grid(column=0, row=5,sticky=E)
    btn5 = ttk.Button(window, text ="Удалить все записи",width=70, command=delete_all)
    btn5.grid(column=0, row=6,sticky=E)
    btn6 = ttk.Button(window, text ="Добавить новую запись",width=70, command=insert_window)
    btn6.grid(column=0, row=7,sticky=E)
    btn7 = ttk.Button(window, text ="Выгрузка в файл",width=70, command=export_data)
    btn7.grid(column=0, row=8,sticky=E)
    btn8 = ttk.Button(window, text ="Загрузка из файла",width=70, command=import_data)
    btn8.grid(column=0, row=9,sticky=E)

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

    tree.column("#1", stretch=NO, width=0)
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

# дублирование записи
def duplicate():
    if tree.selection():
        controller.duplicat_row(id)
        update()

# окно изменения записи    
def update_window():
    if tree.selection():
        title = "Изменить"
        data = datalist
        update = True
        window_constructor(title, data, update)

# окно добавления новой записи  
def insert_window():
    title = "Добавить"
    data = [0,"","","",""]
    update = False
    window_constructor(title, data, update)


# конструктор окна работы с записью
def window_constructor(title, data, update):
        global u_window
        u_window = Toplevel()
        u_window.title(title)
        u_window.geometry("250x200")

        global entry_surname
        global entry_name
        global entry_phone
        global entry_description

        lbl_surname = Label(u_window, text="Фамилия *: ")
        lbl_surname.grid(column=0, row=0,sticky=E)
        entry_surname = Entry(u_window)
        entry_surname.grid(column=1,row=0)
        entry_surname.insert(0,data[1])

        lbl_name = Label(u_window, text="Имя *: ")
        lbl_name.grid(column=0, row=1,sticky=E)
        entry_name = Entry(u_window)
        entry_name.grid(column=1,row=1)
        entry_name.insert(0,data[2])

        lbl_phone = Label(u_window, text="Телефон *: ")
        lbl_phone.grid(column=0, row=2,sticky=E)
        entry_phone = Entry(u_window)
        entry_phone.grid(column=1,row=2)
        entry_phone.insert(0,data[3])

        lbl_description = Label(u_window, text="Описание: ")
        lbl_description.grid(column=0, row=3,sticky=E)
        entry_description = Entry(u_window)
        entry_description.grid(column=1,row=3)
        entry_description.insert(0,data[4])

        if update:
            accept = Button(u_window, text ="Сохранить",width=10, command=save)
        else:
            accept = Button(u_window, text ="Добавить",width=10, command=insert)
        accept.grid(column=1, row=4)
        u_window.grab_set()

# кнопка сохранение изменений  
def save():
    if entry_surname.get() == "" or entry_name.get() == "" or entry_phone.get() == "":
        showerror("Error", message= "Не заполнено обязательное поле!")
    else:
        str_data = (entry_surname.get(),entry_name.get(),entry_phone.get(),entry_description.get(),id)
        controller.update_row(str_data)
        update()
        u_window.grab_release()
        u_window.destroy()

# кнопка добавление записи
def insert():
    if entry_surname.get() == "" or entry_name.get() == "" or entry_phone.get() == "":
        showerror("Error", message= "Не заполнено обязательное поле!")
    else:
        str_data = (entry_surname.get(),entry_name.get(),entry_phone.get(),entry_description.get())
        controller.insert_row(str_data)
        update()
        u_window.grab_release()
        u_window.destroy()  

# удаление записи
def delete_row():
    if tree.selection():
        controller.delete_row(id)
        update()

# удаление всех записей
def delete_all():
    controller.delete_all()
    update()

# выгрузка в файл
def export_data():
    export = True
    title = "Выгрузка"
    dialog_constructor(title,export)

# загрузка из файла
def import_data():
    export = False
    title = "Загрузка"
    dialog_constructor(title,export)

# конструктор окна диалога выгрузки-загрузки
def dialog_constructor(title, export):
    global d_window
    d_window = Toplevel()
    d_window.title(title)
    d_window.geometry("600x100")

    if export:
        lbl_exp = Label(d_window, text="Выбрать формат файла: ")
        formats = ["csv","xml","json"]
        global combo2
        combo2 = ttk.Combobox(d_window, values=formats, state="readonly")
        combo2.grid(column=1,row=0)
        combo2.current(0)
        btn_exp = Button(d_window, text ="Выполнить",width=20, command=exporting)
    
    else:
        btn_exp = Button(d_window, text ="Выполнить",width=20, command=importing)
        lbl_exp = Label(d_window, text="Путь к файлу: ")
        global entry_path
        entry_path = Entry(d_window, width=70)
        entry_path.grid(column=1,row=0)
        open_button = Button(d_window, text ="Выбрать файл",width=20, command=path_file)
        open_button.grid(column=1,row=1,sticky=W)
        
    lbl_exp.grid(column=0, row=0, sticky=E)
    btn_exp.grid(column=1, row=2, sticky=W)
    
    d_window.grab_set()

def exporting():
    type_file = combo2.get()
    controller.export_data(type_file)
    showinfo("Info", message="Данные выгружены в файл data.{}".format(type_file))
    d_window.grab_release()
    d_window.destroy()

def importing():
    if entry_path.get():
        f_path = entry_path.get()
        f_type = f_path[-4::]
        match f_type:
            case "json":
                print('json')
                finish_import()
            case ".xml":
                m = controller.import_xml(f_path)
                if m == "Success":
                    showinfo("Info", message=m)
                else:
                    showerror("Error", message=m)
                finish_import()
            case ".csv":
                m = controller.import_csv(f_path)
                if m == "Success":
                    showinfo("Info", message=m)
                else:
                    showerror("Error", message=m)
                finish_import()
            case _:
                showerror("Error", message= "Не подходящий формат файла!")

    else:
        showerror("Error", message= "Не выбран файл для загрузки!")


# открыть путь к файлу
def path_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        entry_path.insert(0,str(filepath))

# успешный финал импорта
def finish_import():
    # showinfo("Info", message="Данные загружены")
    d_window.grab_release()
    d_window.destroy()
    update()
