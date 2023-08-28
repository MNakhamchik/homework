import sqlite3
from random import randint

conn = sqlite3.connect('hw_6.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_6(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
        

for i in range(2):
    b = randint(1,20)
    cursor.execute('''INSERT INTO tab_6(col_1) VALUES (?)''', (b,))
    conn.commit()

class Home():
    def removal(self):
        cursor.execute('''DELETE FROM tab_6''')
        conn.commit()


num = Home()
num.removal()

cursor.execute('''SELECT * FROM tab_6''')
tabl = cursor.fetchall()
print(tabl)            
