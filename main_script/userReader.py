from main_script.DotsCollectionClass import Dot
import numpy as np

def readUser():
    print("Каким способом Вы хотите ввести данные \n"
          "1) по точкам\n"
          "2) на основе функции")

    dots_mod = int(input())
    if dots_mod == 1:
        print("Введите название файла, в котором находятся точки")
        while True:
            try:
                file_name = input()
                file = open(file_name, 'r')
                break
            except Exception:
                print("Ошибка с файлом")
        dots_list = readPoint(file_name)
    else:
        print("На основе какой функции вы хотите выбрать точки\n"
              "1) f(x) = sin (x)\n"
              "2) f(x) = cos(x)\n"
              "3) f(x) = x^2")
        fun_mod = int(input())
        print("Сколько точек?")
        length = int(input())
        print(f"Введите координаты для x {length} раз")
        dots_list = []
        for i in range(length):
            x = int(input())
            dots_list.append(Dot(x, chooseFunc(x, fun_mod)))



    return dots_list

def readInterpolationPoint ():
    print("Для какого X вы хотите найти значение?")
    X = float(input())
    return X


# чтение из файла
def readPoint(file_name: str) -> list:
    file = open(file_name, 'r')
    dots_list = []
    for line in file:
        try:
            dots = line.split()
            if len(dots) != 2:
                continue
            dot: Dot = Dot(float(dots[0]), float(dots[1]))
            dots_list.append(dot)
        except Exception:
            continue
    file.close()

    return dots_list

def chooseFunc(x, func_mod: int):
    if func_mod == 1:
        return np.sin(x)
    elif func_mod == 2:
        return np.cos(x)
    else:
        return x**2
