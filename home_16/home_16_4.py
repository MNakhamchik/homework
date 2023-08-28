import sqlite3
from random import randint

conn = sqlite3.connect('hw_4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_4(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
        

for i in range(2):
    b = randint(1,20)
    cursor.execute('''INSERT INTO tab_4(col_1) VALUES (?)''', (b,))
    conn.commit()

class Home():
    def removal(self):
        cursor.execute(f'''DELETE FROM tab_4 WHERE id = 4 ''')
        conn.commit()


num = Home()
num.removal()

cursor.execute('''SELECT * FROM tab_4''')
tabl = cursor.fetchall()
print(tabl)            
