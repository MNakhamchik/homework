class Soda():
    def __init__(self, dobavka):
        self.dobavka = dobavka
        if isinstance(self.dobavka, str):
            self.dobavka = dobavka
        else:
            self.dobavka = None

    def show_my_drink(self):
        if self.dobavka:
            print(f'Газировка и добавка {self.dobavka}')
        else:
            print('Обычная газировка')
           
second_drink = Soda('apple')
third_drink = Soda(1)
second_drink.show_my_drink()
third_drink.show_my_drink()
