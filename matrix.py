from random import *

matrix_A = []
matrix_B = []
sum_op = 0

# Программа запрашивает у пользователя размеры прямоугольных матриц 𝐴 и 𝐵, а также параметр k
a1, a2 = list(map(int, input("Введите размер матрицы A (m x n):\n ").split()))
b1, b2 = list(map(int, input("Введите размер матрицы B (n x p):\n ").split()))

k = int(input("Введите значение параметра k:\n "))

# Проверка, что кол-во столбов в первой матрицу равно кол-ву строк второй матрицы
if a2 != b1:
    print("Матрицы таких размеров нельзя перемножить")
# Проверка условия, что m*n не превосходит 30*30
if a1 * a2 > 900:
    print("Матрица А имеет достаточно большой размер")
# Пpоверка уcловия, что n*p не превосходит 30*30
elif b1 * b2 > 900:
    print("Матрица В имеет достаточно большой размер")

else:
    # Получение матрицы А
    for i in range(a1):
        a = []
        matrix_A.append(a)
        for j in range(a2):
            a.append(randint(-9, 9))
    # Получение матрицы В
    for i in range(b1):
        b = []
        matrix_B.append(b)
        for j in range(b2):
            b.append(randint(-9, 9))

    # Вывод матрицы А
    print('Матрица А: ')
    for i in matrix_A:
        print(i)
    # Вывод матрицы В
    print("Матрица B: ")
    for i in matrix_B:
        print(i)
    # Ввод дополнительных данных из имеющихся
    m, n, p = len(matrix_A), len(matrix_A[0]), len(matrix_B[0])

    # Получение матрицы С (Заполнение матрицы 0, а затем прибавление [i][j] элемента)
    matrix_C = [[0 for i in range(p)] for j in range(m)]
    for i in range(m):
        for j in range(p):
            for g in range(n):
                # Считает количество операций сложения
                sum_op += 1
                matrix_C[i][j] += matrix_A[i][g] * matrix_B[g][j]

    # Вывод матрицы С
    print('Матрица С: ')
    for i in range(m):
        print(matrix_C[i])

    # Заметим, для каждого члена матрицы С необходимо на 1 сложение меньше, чем умножение
    print(f"Количество элементарных операций умножения: {sum_op} "
          f"Количество элементарных операций сложения: {sum_op - (n * n)}")
