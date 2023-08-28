class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self,grade):
        self.grades.append(grade)
    
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def is_honors_student(self):
        if self.get_average_grade() > 4.5:
            return True
        else:
            return False
        
name = input('Введите имя: ')
age = int(input('Введите возраст: '))
student = Student(name, age)
grade = int(input('Введите оценку: '))
student.add_grade(grade)
print(student.is_honors_student())