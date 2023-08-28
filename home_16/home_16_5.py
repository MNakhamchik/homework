import sqlite3
from random import randint

conn = sqlite3.connect('hw_5.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_5(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')

for i in range(2):
    b = randint(1,20)
    cursor.execute('''INSERT INTO tab_5(col_1) VALUES (?)''', (b,))
    conn.commit()

        
class Home():
    def hom(data):
        cursor.execute('''SELECT * FROM tab_5''')
        data = cursor.fetchall()
        print("Всего строк:  ", len(data))
        print("Вывод каждой строки")
        for row in data:
            print('ID:', row[0])
            print('Number:',row[1])
        cursor.close()
 
    


num = Home()
num.hom()
