from Methods.AbstractMethod import AbstractMethod
from main_script.DotsCollectionClass import DotsCollection

"""Многочлен Лагранжа"""
class LagrangeMethod(AbstractMethod):
    def __init__(self) -> None:
        super().__init__()

    def begin(self, dots: DotsCollection, num) -> float:

        x_coords, y_coords = [], []
        [(x_coords.append(i.x), y_coords.append(i.y)) for i in dots]

        x = num
        lx = 0

        for i in range(0, len(dots)):
            li = 1

            for j in range(0, len(dots)):
                if i == j:
                    continue
                li *= (x - x_coords[j]) / (x_coords[i] - x_coords[j])
            lx += y_coords[i] * li

        return lx
