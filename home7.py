def dog_func():
    human_age=float(input('Введите Ваш возраст: '))
    if human_age < 0:
        print('Введен неправильный возраст')
        return
    if human_age <= 2:
        dog_age = (10.5 * human_age)
    else:
        human_age > 2 
        dog_age = ((10.5 * 2) + (human_age - 2) * 4)
    print(f'Cобачий возраст {dog_age}')
if __name__=='__main__':
    dog_func()
