line = int(input("Введите количество строк: ")) 
column = int(input("Введите количество столбцов: ")) 

def create(line, column):
    matrix = [[0] * column for _ in range(line)]
    value = 1

    for i in range(line + column - 1):
        if i < line:
            row = i
            col = 0
        else:
            row = line - 1
            col = i - line + 1

        while row >= 0 and col < column:
            matrix[row][col] = value
            value += 1
            row -= 1
            col += 1

    return matrix

def matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


result = create(line, column)
print("Матрица:")
matrix(result)