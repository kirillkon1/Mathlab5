import matplotlib.pyplot as plt
from main_script.DotsCollectionClass import Dot



# метод для отрисовки графика(-ов)
def drawFunction(x_coords: list, y_coords: list, dots: list, interpolarDot: Dot, title=None, color='b') -> None:
    x_coords_dots, y_coords_dots = [], []
    [(x_coords_dots.append(i.x), y_coords_dots.append(i.y)) for i in dots]

    ax = plt.gca()
    # x_coords.append(interpolarDot.x)
    # y_coords.append(interpolarDot.y)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(x_coords, y_coords)
    plt.title(title)
    plt.scatter(x_coords_dots, y_coords_dots)

    # if not interpolarDot.x < min(x_coords) and not interpolarDot.x > max(x_coords):
    plt.scatter([interpolarDot.x], [interpolarDot.y], edgecolors= 'r')


    plt.show()
