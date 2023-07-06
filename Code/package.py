#####
import math

import numpy as np


####Definiowanie dzialania na kwaternionach
# Iloczyn skalarny
def dotProduct(x: list, y: list):
    sum1 = x[0] * y[0] + x[1] * y[1] + x[2] * y[2]
    return sum1


# Norma Kwaternionu
def normOfQuaternion(a: float, vector: list):
    i = 0
    sum = a**2
    while i < 3:
        sum = (vector[i]) ** 2 + sum
        i = i + 1
    return sum


# Dodawanie wektorów
def addingVectorPart(x: list, y: list):
    sum2 = [x[0] + y[0], x[1] + y[1], x[2] + y[2]]
    return sum2


# Iloczyn wektorowy
def crossProduct(x: list, y: list):
    e1 = x[1] * y[2] - x[2] * y[1]
    e2 = (x[0] * y[2] - x[2] * y[0]) * (-1)
    e3 = x[0] * y[1] - x[1] * y[0]
    list_return = [e1, e2, e3]
    return list_return


# Iloczyn skalarny
def scalarVector(a: float, x: list):
    lista = [a * x[0], a * x[1], a * x[2]]
    return lista


# Mnożenie Kwaternionów
def multiQuaternion(a1: float, x1: list, a2: float, x2: list):
    f1 = a1 * a2
    f4 = crossProduct(x1, x2)
    f2 = dotProduct(x1, x2)
    f3_a = scalarVector(a2, x1)
    f3_b = scalarVector(a1, x2)
    f3 = addingVectorPart(f3_a, f3_b)
    return [f1 - f2, addingVectorPart(f3, f4)]


# Normalizacja Wektora
def NormalizeVector(x: list):
    l = (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** (1 / 2)
    return [1 / l * x[0], 1 / l * x[1], 1 / l * x[2]]


# Sprzeżenie kwaternionu
def conjugateQuaternion(a: float, vector: list):
    scalar = a
    vector_1 = scalarVector(-1, vector)
    return [a, vector_1]


### Rotacja macierzowa
# Macierz obrotu względem osi x
def xaxisMatrixrotation(angle: float):
    RotationMatrix = np.array(
        [
            [1, 0, 0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle), math.cos(angle)],
        ]
    )
    return RotationMatrix


# Macierz obrotu względem osi y
def yaxisMatrixrotation(angle: float):
    RotationMatrix = np.array(
        [
            [math.cos(angle), 0, math.sin(angle)],
            [0, 1, 0],
            [-math.sin(angle), 0, math.cos(angle)],
        ]
    )
    return RotationMatrix


# Macierz obrotu względem osi z
def zaxisMatrixrotation(angle: float):
    RotationMatrix = np.array(
        [
            [math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0, 1],
        ]
    )
    return RotationMatrix


# Macierz obrotu względem kąta eulera (z,y,x)
def rotationMatrixZYX(z_angle: float, y_angle: float, x_angle: float):
    z_matrix = zaxisMatrixrotation(z_angle)
    y_matrix = yaxisMatrixrotation(y_angle)
    x_matrix = xaxisMatrixrotation(x_angle)
    return np.matmul(z_matrix, np.matmul(y_matrix, x_matrix))
