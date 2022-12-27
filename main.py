import user_interface
import controller

controller.open_db()
ds = controller.all_rows()
user_interface.open(ds)

# name = input('Укажите имя: ')
# surname = input('Укажите фамилию: ')
# phone = input('Укажите номер телефона: ')
# description = input('Укажите описание: ')

# str_data = (surname,name,phone,description)

# new_conn = db.create_connection()
# row = data_crud.insert_row(new_conn,str_data)
# db.close_connection(new_conn)
# print(row)

# id = int(input('Укажите номер записи: '))
# name = input('Укажите новое имя: ')
# surname = input('Укажите новую фамилию: ')
# phone = input('Укажите новый номер телефона: ')
# description = input('Укажите новое описание: ')

# str_data = (surname,name,phone,description,id)

# id = int(input('Укажите номер записи: '))
# new_conn = db.create_connection()
# data_crud.delete_row(new_conn,id)
# db.close_connection(new_conn)


# for r in rows:
#     print(r)


# id = int(input('Указать номер строки для отображения '))
# new_conn = db.create_connection()
# r = data_crud.select_rowid(new_conn,id)
# db.close_connection(new_conn)
# print(r)

