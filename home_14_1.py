import sqlite3
from random import randint

conn = sqlite3.connect('hw_14.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
b = randint(1,20)

for i in range(4):
    cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (b,))
    conn.commit()


class Database():
    def argument(*args):
        
        if len(args) == 1:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
            conn.commit()
        elif len(args) == 2 :
                type(args[1]) == int or type(args[1]) == float
                cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
                conn.commit()
        elif len(args) == 3:
            type(args[0]) == None and type(args[1]) == None and type(args[3]) == int
            cursor.execute('''UPDATE tab_1 SET col_1 = '77' WHERE id = 3''')
            conn.commit()
        else:
            pass  
        

num = Database()
num.argument(1)
num.argument(1,2)


cursor.execute('''SELECT * FROM tab_1''')
tabl = cursor.fetchall()
print(tabl)            
