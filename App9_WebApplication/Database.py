import sqlite3

def connect():
    conn=sqlite3.connect("WebAppFinal.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS IdData (id INTEGER PRIMARY KEY,email Text,height INTEGER,weight INTEGER)")
    conn.commit()
    conn.close()

def insert_record(email,height,weight):
    conn=sqlite3.connect("WebAppFinal.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO IdData VALUES(NULL,?,?,?)",(email,height,weight))
    conn.commit()
    cur.close()

def display_all():
    conn=sqlite3.connect("WebAppFinal.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM IdData")
    records=cur.fetchall()
    conn.close()
    return records

def flush_Db():
    conn=sqlite3.connect("WebAppFinal.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM IdData")
    conn.commit()
    conn.close()
    
connect()
