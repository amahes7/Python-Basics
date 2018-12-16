import sqlite3

def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title Text,author Text,year INTEGER, ISBN INTEGER, pages INTEGER,genre Text)")
    conn.commit()
    conn.close()

def display_all():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    records=cur.fetchall()
    conn.close()
    return records

def insert_record(title,author,year,isbn,pages,genre):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?,?,?)",(title,author,year,isbn,pages,genre))
    conn.commit()
    cur.close()


def search_record(title,author,year,isbn,pages,genre):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=? OR pages=? OR genre = ?",(title,author,year,isbn,pages,genre))
    result=cur.fetchall()
    conn.close()
    return result

def delete_record(id):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update_record(id,title,author,year,isbn,pages,genre):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?,year=?,isbn=?,pages=?,genre=? WHERE id=?",(title,author,year,isbn,pages,genre,id))
    conn.commit()
    conn.close()

connect()
#delete_record(100)

#print(search_record(author="Maheshwari"))
#insert_record("Abhijeet","Maheshwari",1889,1001)
#update_record(1,"Abhijeet","Maheshwari",1889,1002)
#print(display_all())
