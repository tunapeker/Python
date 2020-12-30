import sqlite3
import time
class Book():
    def __init__(self,isim,yazar,sayfa_sayisi,baski):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.baski = baski
    def __str__(self):
        return "Name:{}\nAuthor:{}\nPage number:{}\nEdition:{}".format(self.isim,self.yazar,self.sayfa_sayisi,self.baski)
class Library():
    def __init__(self):
        self.connect()
    def connect(self):
        self.con = sqlite3.connect("library.db")
        self.cursor = self.con.cursor()
        command = "CREATE TABLE IF NOT EXISTS books (isim TEXT,yazar TEXT,sayfa_sayisi INT,baski INT)"
        self.cursor.execute(command)
        self.con.commit()
    def add_book(self,book):
        command = "INSERT INTO books VALUES(?,?,?,?)"
        self.cursor.execute(command,(book.isim,book.yazar,book.sayfa_sayisi,book.baski))
        self.con.commit()
    def select_all_data(self):
        command = "SELECT * FROM books"
        self.cursor.execute(command)
        lst = self.cursor.fetchall()
        if len(lst) == 0:
            print("There is no book in the library.")
        else:
            for i in lst:
                print(i)
    def connection_stop(self):
        self.con.close()
    def select_data(self,isim):
        command = "SELECT * FROM books WHERE isim = ?"
        self.cursor.execute(command,(isim,))
        lst = self.cursor.fetchall()
        if len(lst) == 0:
            print("There is not a book named {}.".format(isim))
        else:
            for i in lst:
                print(i)
    def delete_book(self,isim):
        command = "DELETE FROM books WHERE isim = ?"
        self.cursor.execute(command,(isim,))
        self.con.commit()
