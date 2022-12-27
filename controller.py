import data_crud
import db

def open_db():
    db.create_my_phonebook()

# запрос всех записей из базы
def all_rows():
    new_conn = db.create_connection()
    rows = data_crud.select_all(new_conn)
    db.close_connection(new_conn)
    dataset = [d for d in rows]
    return dataset

# поиск записей по условию
def find_rows(find_field,find_str):
    new_conn = db.create_connection()
    find_rows = data_crud.select_param(new_conn,find_field,find_str)
    db.close_connection(new_conn)
    dataset = [d for d in find_rows]
    return dataset

# дублирование записи
def duplicat_row(id):
    new_conn = db.create_connection()
    new_row = data_crud.select_rowid(new_conn, id)
    new_data = (new_row[1], new_row[2], new_row[3], new_row[4])
    data_crud.insert_row(new_conn,new_data)
    db.close_connection(new_conn)

def update_row(data):
    new_conn = db.create_connection()
    data_crud.update_row(new_conn,data)
    db.close_connection(new_conn)