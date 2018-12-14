import sqlite3

def create_table():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE uic (name TEXT,uin INTEGER)")
    conn.commit()
    conn.close()

def insert_data(name,id):
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO uic VALUES (?,?)",(name,id))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM uic")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_record(uin):
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM uic WHERE uin =?",(uin,))
    conn.commit()
    conn.close()

def update(uin,name):
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute("UPDATE uic SET uin =? WHERE name=?",(uin,name,))
    conn.commit()
    conn.close()


#delete_record(650810)
#insert_data("Abhi ",6508)
#update(650810,"jeetu ")
print("Table Data:",view())
    