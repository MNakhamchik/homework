class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    

    def get_perimeter(self):
        perimetr = 2 * (self.width + self.height)
        return perimetr
    
w_width = input('Введите width: ')
h_height = input('Введите height: ')

a = Rectangle(float(w_width),float(h_height))

print(f'Площадь равна: ', a.get_area())
print(f'Периметр равен: ',a.get_perimeter())