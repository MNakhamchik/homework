class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        return print('Заработная плата сотрудника', self.name, 'составляет: ', self.salary,)
    
    def get_tax(self):
            return float(self.salary) * 0.2
            

name_a = input('Введите имя сотрудника: ')
salary_a = int(input('Укажите з/п сотрудника : '))
position_a = input('Укажите должность сотрудника: ')

emp = Employee(name_a, position_a, salary_a)
emp.get_salary()
emp.get_tax()
print('Сумма налога: ', emp.get_tax())