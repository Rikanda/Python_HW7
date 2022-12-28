

def insert_row(conn, my_data):
    c = conn.cursor()
    sql = "INSERT INTO phonebook (surname,name,phone,description) VALUES (?,?,?,?)"
    c.execute(sql, my_data)
    conn.commit()
    return c.lastrowid

def update_row(conn, my_data):
    c = conn.cursor()
    sql = 'UPDATE phonebook SET surname = ? , name =? , phone = ? , description = ? WHERE id = ?'
    c.execute(sql, my_data)
    conn.commit()
    return c.rowcount


def select_rowid(conn,id):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook WHERE id = ?',(id,))
    r = c.fetchone()
    return r

def select_all(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM phonebook')
    rows = c.fetchall()
    return rows

def select_param(conn, param, find_text):
    c = conn.cursor()
    sql_text = f'SELECT * FROM phonebook WHERE {param} like "%{find_text}%"'
    c.execute(sql_text)
    rows = c.fetchall()
    return rows

def delete_row(conn,id):
    c = conn.cursor()
    c.execute('DELETE FROM phonebook WHERE id = ?',(id,))
    conn.commit()

def clear_all(conn):
    c = conn.cursor()
    c.execute('DELETE FROM phonebook')
    conn.commit()
