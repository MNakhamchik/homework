import sqlite3

conn = sqlite3.connect('hw_1.db')
cursor = conn.cursor()

  

class Home:
    def __init__(self, name):
        self.name = name
    def hom(self):
        cursor.execute(f'''SELECT count(name) FROM sqlite_master WHERE TYPE= 'table' AND name= '{self.name}' ''') 
        if cursor.fetchone()[0] == 1: 
            print('Таблица уже существует!')
        else:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.name} (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 TEXT)''')
            conn.commit()

tab_a = Home('tabl')
tab_a.hom()
tabl = cursor.fetchall()
print(tabl)