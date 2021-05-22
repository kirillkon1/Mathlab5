from DotsCollectionClass import *
from Methods.LagrangeMethod import LagrangeMethod
from Methods.NewtonMethod import NewtonMethod
from main_script.Drawer import drawFunction
from main_script.userReader import readUser, readInterpolationPoint

dots = readUser()

# dots = sin_dots

x_list = [i.x for i in dots]
X1, X2 = 1.15, 1.852

if __name__ == '__main__':
    interpolarDot = readInterpolationPoint()  # X, который нужно найти

    # interpolarDot = X2

    min_x, max_x = min(x_list), max(x_list)

    print("X |", *[f"{toFixed(i.x):>3} |" for i in dots])
    print("Y |", *[f"{toFixed(i.y):>3} |" for i in dots])

    flag_largrange = True
    lagrange_method = LagrangeMethod()
    newton_method = NewtonMethod()

    result_dot_lagrange = ''
    try:
        result_dot_lagrange = Dot(interpolarDot, lagrange_method.begin(dots, interpolarDot))
    except Exception:
        flag_largrange = False

    if not flag_largrange:
        print("Ошибка в многочлене Лагранжа")

    result_dot_newton = Dot(interpolarDot, newton_method.begin(dots, interpolarDot))

    print("result_dot_newton ", result_dot_newton)

    x_coords = []
    y_coords_Lagrange = []
    y_coords_Newton = []

    setup = 0.1
    step = 0.05

    for i in np.arange(min_x - setup, max_x + setup, step):
        i_tmp = np.around(i, 2)
        x_coords.append(i_tmp)
        if flag_largrange:
            y_coords_Lagrange.append(np.around(lagrange_method.begin(dots, i_tmp), 4))
        y_coords_Newton.append(np.around(newton_method.begin(dots, i_tmp), 4))

    # if not interpolarDot < min(x_coords) and not interpolarDot > max(x_coords):
    if flag_largrange:
        drawFunction(x_coords, y_coords_Lagrange, dots, result_dot_lagrange, "Интерполяция методом Лагранжа", 'orange')
    drawFunction(x_coords, y_coords_Newton, dots, result_dot_newton,
                 "Интерполяция методом Ньютона (Конечные разности)")
    # else:
    # print("Точка находится вне области")
