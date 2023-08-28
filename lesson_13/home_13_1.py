class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def hello(self):
        print(f'Привет,меня зовут {self.name} и мне {self.age} лет')


name = input('Введите имя: ')    
age = input('Введите возраст: ') 
human = Person(name, age)
human.hello()