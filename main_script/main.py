from DotsCollectionClass import *
from Methods.LagrangeMethod import LagrangeMethod
from Methods.NewtonMethod import NewtonMethod
from main_script.Drawer import drawFunction
from main_script.userReader import readUser, readInterpolationPoint

# dots = readUser()

dots = cos_20dots

x_list = [i.x for i in dots]
X1, X2 = 1.15, 1.852

if __name__ == '__main__':

    interpolarDot = readInterpolationPoint()  # X, который нужно найти

    min_x, max_x = min(x_list), max(x_list)

    lagrange_method = LagrangeMethod()
    newton_method = NewtonMethod()
    result_dot_lagrange = Dot(interpolarDot, lagrange_method.begin(dots, interpolarDot))
    result_dot_newton = Dot(interpolarDot, newton_method.begin(dots, interpolarDot))

    x_coords = []
    y_coords_Lagrange = []
    y_coords_Newton = []

    setup = 0.1
    step = 0.05

    for i in np.arange(min_x - setup, max_x + setup, step):
        i_tmp = np.around(i, 2)
        x_coords.append(i_tmp)
        y_coords_Lagrange.append(np.around(lagrange_method.begin(dots, i_tmp), 4))
        y_coords_Newton.append(np.around(newton_method.begin(dots, i_tmp), 4))

    if not interpolarDot < min(x_coords) and not interpolarDot > max(x_coords):

        drawFunction(x_coords, y_coords_Lagrange, dots, result_dot_lagrange, "Интерполяция методом Лагранжа", 'orange')
        drawFunction(x_coords, y_coords_Newton, dots, result_dot_newton,
                     "Интерполяция методом Ньютона (Конечные разности)", 'r')
    else:
        print("Точка находится вне области")
