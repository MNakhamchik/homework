import sqlite3
from random import randint
number = randint(0,10)

conn = sqlite3.connect('hw_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_3(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 TEXT)''')
conn.commit()
name = input('Введите имя:')

class Home():
    def __init__(self, numb, name):
        self.numb = numb
        self.name = name

    def hom(self):
        cursor.execute(f'''UPDATE tab_3 SET col_2 = '{name}' WHERE id = 9''')
        conn.commit()

tab_a = Home(number,name)
tab_a.hom()
cursor.execute('''SELECT * FROM tab_3''')
tabl = cursor.fetchall()
print(tabl)  