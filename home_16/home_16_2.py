import sqlite3
from random import randint
number = randint(0,10)

conn = sqlite3.connect('hw_2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 TEXT)''')
conn.commit()

class Home():
    def __init__(self, id, name):
        self.id = id
        self.name = name 
    
    def hom(self):
            info = cursor.execute('SELECT * FROM tab_2 WHERE col_1 ')
            try:
                info.fetchone() is None
                print(f'Ошибка, id {self.id} уже существует')
            except:
                cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 TEXT)''')
                conn.commit()


a = Home(number,'Anna')
a.hom()

cursor.execute('''SELECT * FROM tab_2''')
tabl = cursor.fetchall()
print(tabl)  