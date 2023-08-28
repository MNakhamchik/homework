# список для наполнения(числа, среди которых будем искать)
nums = []

# проверяем число target. Если условие верное , то идем дальше, если нет , то ошибка и заново вводим
while True:
    try:
        target = int(input('Введите число, которое будем искать:'))
        if -109 <= target <= 109:
            break
        else:
            print('Необходимы числа от -109 до 109')
    except:
        print('Ошибка')


# проверяем длинну списка nums, если < 2 то добавляем , если  > 104 то ошибка,
while True:
    try:
        if len(nums) <= 2:
            sm = int(input('Введите число, для поиска суммы:'))
            if -109 <= sm <= 109:
                nums.append(sm)
            else:
                print('Необходимы числа от -109 до 109')
        elif 2 <= len(nums) <= 104:
            sm1 = int(input('Введите число, для поиска суммы:'))
            if -109 <= sm1 <= 109:
                nums.append(sm1)
            else:
                print('Необходимы числа от -109 до 109')
        elif 104 < len(nums):
            print('Вы ввели максимальное кол-во чисел.')
            break
    except:
        break


def sumnum(nums, target):
    no_pair = 'Нет пары, которая в сумме будет равняться target'
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                no_pair = f'Ответ [{i},{j}]'
    return no_pair


print(sumnum(nums, target))