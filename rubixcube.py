from copy import copy
import numpy as np

# colors: Y(ellow),  O(range),   B(lue),     R(ed),     G(reen),    W(hite)
# faces:  0: UP,     1: FRONT,   2: RIGHT,   3: BACK,   4: LEFT,    5: DOWN


class RubixCube:
    def __init__(self, cube=None):
        if cube is None:
            cube = np.array([[["Y"] * 3] * 3, [["O"] * 3] * 3, [["B"] * 3] * 3, [["R"] * 3] * 3, [["G"] * 3] * 3,
                    [["W"] * 3] * 3])
        self.cube = cube

    def rotate_F(self):
        self.cube[1] = np.rot90(self.cube[1], 3)
        temp = np.copy(self.cube[0][2])  # save up
        for i in range(0, 3):  # write left into up
            self.cube[0][2][i] = self.cube[4][2-i][2]
        for i in range(0, 3):
            self.cube[4][i][2] = self.cube[5][0][i]  # write down into left
        for i in range(0, 3):  # write right into down
            self.cube[5][0][i] = self.cube[2][2-i][0]
        for i in range(0, 3):
            self.cube[2][i][0] = temp[i]  # write up(temp) into right

    def rotate_R(self):
        self.cube[2] = np.rot90(self.cube[2], 3)
        temp = np.copy(self.cube[1][:][2])  # save O
        for i in range(0, 3):
            self.cube[1][i][2] = self.cube[5][i][2]
        for i in range(0, 3):
            self.cube[5][i][2] = self.cube[3][2-i][0]
        for i in range(0, 3):
            self.cube[3][i][0] = self.cube[0][2-i][2]
        for i in range(0, 3):
            self.cube[0][i][2] = temp[i]

    def rotate_U(self):
        self.cube[0] = np.rot90(self.cube[0], 1)
        temp = np.copy(self.cube[3][0])
        self.cube[3][0] = self.cube[4][0][::-1]
        self.cube[4][0] = self.cube[1][0]
        self.cube[1][0] = self.cube[2][0]
        self.cube[2][0] = temp

    def rotate_L(self):
        self.cube[4] = np.rot90(self.cube[4], 3)
        temp = copy(self.cube[0][:][0])[::-1]
        for i in range(0, 3):
            self.cube[0][i][0] = self.cube[1][i][0]
        for i in range(0, 3):
            self.cube[1][i][0] = self.cube[5][i][0]
        for i in range(0, 3):
            self.cube[5][i][0] = self.cube[3][i][2]
        for i in range(0, 3):
            self.cube[3][i][2] = temp[i]

    def rotate_D(self):
        return NotImplementedError

    def print_cube(self):
        face_name = ["UP", "FRONT", "RIGHT", "BACK", "LEFT", "DOWN"]
        print("---------------CUBE---------------")
        for i in range(0, len(self.cube)):
            print(f"For {face_name[i]}-face the configuration is currently:")
            for j in range(0, len(self.cube[i])):
                print(self.cube[i][j])
        print("----------------------------------")

    def print_face(self, face=0):
        print("---------------FACE---------------")
        above = self.cube[3][0][::-1]
        below = self.cube[1][0]
        left = self.cube[2][0][::1]
        right = self.cube[4][0]
        if face == 1:
            above = self.cube[0][2]
            below = self.cube[5][0]
            left = self.cube[4][:][2]
            right = self.cube[2][:][0]
        elif face == 2:
            above = self.cube[3][0][::-1]
            below = self.cube[1][0]
            left = self.cube[2][0][::1]
            right = self.cube[4][0]
        elif face == 3:
            above = self.cube[3][0][::-1]
            below = self.cube[1][0]
            left = self.cube[2][0][::1]
            right = self.cube[4][0]
        elif face == 4:
            above = self.cube[3][0][::-1]
            below = self.cube[1][0]
            left = self.cube[2][0][::1]
            right = self.cube[4][0]
        elif face == 5:
            above = self.cube[3][0][::-1]
            below = self.cube[1][0]
            left = self.cube[2][0][::1]
            right = self.cube[4][0]
        print("   " + str(above))
        for i in range(0, 3):
            print(str(left[i]) + str(self.cube[face][i]) + str(right[i]))
        print("   " + str(below))
        print("----------------------------------")
