# import sqlite3
# from random import randint

# conn = sqlite3.connect('hw_14.db')
# cursor = conn.cursor()


# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')


# for i in range(4):
#     b = randint(1,20)
#     cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (b,))
#     conn.commit()


# class Database():
#     def argument(*args):
        
#         if len(args) == 1:
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
#             conn.commit()
#         elif len(args) == 2 :
#                 type(args[1]) == int or type(args[1]) == float
#                 cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
#                 conn.commit()
#         elif len(args) == 3:
#             type(args[0]) == None and type(args[1]) == None and type(args[3]) == int
#             cursor.execute('''UPDATE tab_1 SET col_1 = '77' WHERE id = 3''')
#             conn.commit()
#         else:
#             pass  
        

# num = Database()
# num.argument(1)
# num.argument(1,2)


# cursor.execute('''SELECT * FROM tab_1''')
# tabl = cursor.fetchall()
# print(tabl)            

import sqlite3

conn = sqlite3.connect('zadacha4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS zadacha_4 (id INTEGER PRIMARY KEY, col_1 TEXT)''') #ключ primary key содержит в себе констр. unique под капотом

#i = int(input('Введите число:')) #заполнила таблицу, чтобы было с чем работать
#for el in range(1,i+1):
#    cursor.execute('''INSERT INTO zadacha_4(id) VALUES (?)''', (el,))
#    conn.commit()

class DeleteData:
    
    def __init__(self, id):
        self.id = id
        
    def delete_data(self):
            cursor.execute(f'''DELETE FROM zadacha_4 WHERE id = {self.id}''')

            conn.commit()
a = DeleteData(1)
a.delete_data()

cursor.execute('''SELECT * FROM zadacha_4''')
k = cursor.fetchall()
print(k)