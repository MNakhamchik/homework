class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year 
        self.speed = speed
    
    def accelerate(self, increase_in_speed):
        self.speed = self.speed + increase_in_speed
            
    def brake(self,speed_reduction):
        self.speed = self.speed - speed_reduction

    def get_speed(self):
        return print(self.speed)


make_car = input('Марка вашей машины: ')
model_car = input('Модель вашей машины: ')
year_car = input('Год выпуска вашей машины: ')
speed_car = int(input('Скорость вашей машины: '))
car = Car(make_car, model_car, year_car, speed_car)
increase_in_speed = int(input('Cкорость увеличится на: '))
car.accelerate(increase_in_speed)  
speed_reduction = int(input('Cкорость снизится на: '))
car.brake(speed_reduction)        
print(f'Скорость вашей машины: ',car.speed)