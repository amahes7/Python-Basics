import sqlite3


class Database:

    def __init__(self):
        self.conn=sqlite3.connect("bookstore.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title Text,author Text,year INTEGER, ISBN INTEGER, pages INTEGER,genre Text)")
        self.conn.commit()

    def display_all(self):
        self.cur.execute("SELECT * FROM books")
        records=self.cur.fetchall()
        return records

    def insert_record(self,title,author,year,isbn,pages,genre):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?,?,?)",(title,author,year,isbn,pages,genre))
        self.conn.commit()


    def search_record(self,title,author,year,isbn,pages,genre):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=? OR pages=? OR genre = ?",(title,author,year,isbn,pages,genre))
        result=self.cur.fetchall()
        return result

    def delete_record(self,id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.conn.commit()

    def update_record(self,id,title,author,year,isbn,pages,genre):
        self.cur.execute("UPDATE books SET title=?, author=?,year=?,isbn=?,pages=?,genre=? WHERE id=?",(title,author,year,isbn,pages,genre,id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()

    #delete_record(100)

    #print(search_record(author="Maheshwari"))
    #insert_record("Abhijeet","Maheshwari",1889,1001)
    #update_record(1,"Abhijeet","Maheshwari",1889,1002)
    #print(display_all())
