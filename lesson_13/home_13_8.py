class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def hello(self):
        print(f'Привет,меня зовут {self.name} и мне {self.age} лет')
    
    def can_vote(self):
        if int(self.age) >= 18:
            return True
        else:
            return False


name = input('Введите имя: ')    
age = input('Введите возраст: ') 
human = Person(name, age)
human.hello()
human.can_vote()
print(human.can_vote())