import numpy as np


class Dot:
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


class DotsCollection(list):
    def __init__(self) -> None:
        super().__init__()

    def append(self, __object: Dot) -> None:
        super().append(__object)


# --- Списки точек для примера ---
sin_dots = [Dot(-3, -0.14), Dot(-2, -0.91), Dot(-1, -0.84), Dot(0, 0.0), Dot(1, 0.84), Dot(2, 0.91), Dot(-3, -0.14),
            ]

cos_10dots = [Dot(2.76, -0.93), Dot(-4.42, -0.29), Dot(-3.37, -0.97), Dot(-1.03, 0.51), Dot(-1.84, -0.27),
              Dot(3.0, -0.99), Dot(-2.18, -0.57), Dot(-4.85, 0.14), Dot(4.42, -0.29), Dot(1.45, 0.12),
              ]

cos_20dots = [Dot(-5.0, 0.56), Dot(-4.5, -0.42), Dot(-4.0, -1.3), Dot(-3.5, -1.88), Dot(-3.0, -1.98),
              Dot(-2.5, -1.6),
              Dot(-2.0, -0.84), Dot(-1.5, 0.14), Dot(-1.0, 1.08), Dot(-0.5, 1.76), Dot(0.0, 2.0), Dot(0.5, 1.76),
              Dot(1.0, 1.08), Dot(1.5, 0.14), Dot(2.0, -0.84), Dot(2.5, -1.6), Dot(3.0, -1.98), Dot(3.5, -1.88),
              Dot(4.0, -1.3), Dot(4.5, -0.42)
              ]

sqr_8dots = [Dot(0.27, 0.0729), Dot(8.79, 77.2641), Dot(8.52, 72.5904), Dot(4.34, 18.8356), Dot(7.53, 56.7009),
             Dot(14.89, 221.7121), Dot(4.55, 20.7025), Dot(8.07, 65.1249)]

sqr_8dots_same = [Dot(0, 0), Dot(1, 1), Dot(2, 4), Dot(3, 9), Dot(4, 16),
                  Dot(5, 25), Dot(6, 36), Dot(7, 49)]


def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"


def dots_generator():
    length = 8
    _dots_list = []
    for i in np.arange(-3, 3, 1):
        _dots_list.append(Dot(i, float(toFixed(np.sin(i)))))
        print(f"Dot{i, float(toFixed(np.sin(i)))},", end='')
    return _dots_list


dots_list = []  # хардкод точек
