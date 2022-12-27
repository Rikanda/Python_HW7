import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    if conn:
        conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_my_phonebook():
    sql_create_phonebook_table = """CREATE TABLE IF NOT EXISTS phonebook (
                                        id integer PRIMARY KEY,
                                        surname text NOT NULL,
                                        name text NOT NULL,
                                        phone text NOT NULL,
                                        description text
                                    );  """
    conn = create_connection()
    if conn is not None:
        create_table(conn, sql_create_phonebook_table)
        print('Таблица для записи справочника доступна для работы')
    else:
        print('Ошибка! Системе не удалось подключить базу данных')




