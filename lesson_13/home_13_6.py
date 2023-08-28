class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print('Гав-гав')
    
    def get_human_age(self):
        if int(self.age) <= 0:
            print('Введен неправильный возраст')
            return
        if self.age > 0:
            return 7 * self.age
        

name_a = input('Введите имя собаки: ')
breed_a = input('Введите породу собаки: ')
age_a = int(input('Введите возраст собаки: '))
dog = Dog(name_a, breed_a, age_a)
dog.bark()
print('Возраст собаки в человеческих годах равен: ', dog.get_human_age())
