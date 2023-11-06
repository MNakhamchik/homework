def square(width, height, coordinate):
    area = width * height
    area_1 = 0

    for i in coordinate:
        x1, y1, x2, y2 = i
        area_1 += (x2 - x1) * (y2 - y1)

    area_2 = area - area_1
    return area_2    


width = int(input("Введите ширину матрицы: "))
height = int(input("Введите высоту матрицы: "))
rectangle = int(input("Введите количество прямоугольников: "))

coordinate = []

for i in range(rectangle):
    pair = map(int, input("Введите пары координат(x1, y1, x2, y2): ").split())
    coordinate.append((pair))



area_2 = square(width, height, coordinate)
print(f"Незакрашенная площадь холста: {area_2}")


