from Methods.AbstractMethod import AbstractMethod
from numpy import *

"""Многочлен Ньютона с конечными разностями"""


class NewtonMethod(AbstractMethod):
    def __init__(self) -> None:
        super().__init__()

    def begin(self, dots: list, num) -> float:
        x_coords, y_coords = [], []
        [(x_coords.append(i.x), y_coords.append(i.y)) for i in dots]

        h = x_coords[1] - x_coords[0]

        differences = self.getMatrixOfDifferences(dots)[0]

        Nn = 0
        base = 1


        for i in range(len(dots)):
            Nn += differences[i] * base
            base *= (num - x_coords[i])/(h * (i+1))

        return Nn

    @staticmethod
    def getMatrixOfDifferences(dots: list) -> list:
        k = len(dots)
        x_coords, y_coords = [], []
        [(x_coords.append(i.x), y_coords.append(i.y)) for i in dots]

        table = [[0 for i in range(k)] for j in range(k)]

        for i in range(k):
            table[i][0] = y_coords[i]

        for i in range(1, k):
            for j in range(k - i):
                table[j][i] = table[j + 1][i - 1] - table[j][i - 1]

        # for i in range(len(table)):
        #     print(*[f"{toFixed(x):>7}" for x in table[i]])

        return table


def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"


def fact(n):
    if n == 0:
        return 1
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
