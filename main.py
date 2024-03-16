import rubixcube
import numpy as np


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    # colors: Y(ellow), O(range), B(lue), R(ed), G(reen), W(hite)
    a = np.array([[["Y00", "Y01", "Y02"], ["Y10", "Y11", "Y12"], ["Y20", "Y21", "Y22"]], [["O00", "O01", "O02"], ["O10", "O11", "O12"], ["O20", "O21", "O22"]]
                     , [["B00", "B01", "B02"], ["B10", "B11", "B12"], ["B20", "B21", "B22"]], [["R00", "R01", "R02"], ["R10", "R11", "R12"], ["R20", "R21", "R22"]]
                     , [["G00", "G01", "G02"], ["G10", "G11", "G12"], ["G20", "G21", "G22"]], [["W00", "W01", "W02"], ["W10", "W11", "W12"], ["W20", "W21", "W22"]]])
    b = np.copy(a)
    cube = rubixcube.RubixCube(a)
    cube.print_face(5)
    for i in range(0, 4):
        cube.rotate_D()
        cube.print_face(5)
    functions = [cube.rotate_F, cube.rotate_R, cube.rotate_U, cube.rotate_L, cube.rotate_D]
    for func in functions:
        for i in range(0, 4):
            func()

        if (cube.cube == b).all():
            print("Yeah")
        else:
            print(func)
            cube.print_cube()

