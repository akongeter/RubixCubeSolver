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

    def rotate_clockwise(self, face_to_rotate_by, side_faces):
        self.cube[face_to_rotate_by] = np.rot90(self.cube[face_to_rotate_by], 3)
        
        temp = copy(self.cube[side_faces[0]][2])
        self.cube[side_faces[0]][2] = self.cube[side_faces[1]][:][2][::-1]
        for i in range(0, 3):
            self.cube[side_faces[1]][i][2] = self.cube[side_faces[2]][0][i]
        self.cube[side_faces[2]][0] = self.cube[side_faces[3]][:][0][::-1]
        for i in range(0, 3):
            self.cube[side_faces[3]][i][0] = temp[i]

    def rotate_F(self, clockwise=True):
        self.rotate_clockwise(1, [0, 4, 5, 2])

    def rotate_R(self):
        self.cube[1] = np.rot90(self.cube[1], 3)
        temp = copy(self.cube[0][2])  # save up
        self.cube[0][2] = self.cube[4][:][2][::-1]  # write left into up
        for i in range(0, 3):
            self.cube[4][i][2] = self.cube[5][0][i]  # write down into left
        self.cube[5][0] = self.cube[2][:][0][::-1]  # write right into down
        for i in range(0, 3):
            self.cube[2][i][0] = temp[i]  # write up(temp) into right

    def rotate_U(self):
        self.cube[1] = np.rot90(self.cube[1], 3)
        temp = copy(self.cube[0][2])  # save up
        self.cube[0][2] = self.cube[4][:][2][::-1]  # write left into up
        for i in range(0, 3):
            self.cube[4][i][2] = self.cube[5][0][i]  # write down into left
        self.cube[5][0] = self.cube[2][:][0][::-1]  # write right into down
        for i in range(0, 3):
            self.cube[2][i][0] = temp[i]  # write up(temp) into right

    def rotate_L(self):
        self.cube[1] = np.rot90(self.cube[1], 3)
        temp = copy(self.cube[0][2])  # save up
        self.cube[0][2] = self.cube[4][:][2][::-1]  # write left into up
        for i in range(0, 3):
            self.cube[4][i][2] = self.cube[5][0][i]  # write down into left
        self.cube[5][0] = self.cube[2][:][0][::-1]  # write right into down
        for i in range(0, 3):
            self.cube[2][i][0] = temp[i]  # write up(temp) into right

    def rotate_D(self):
        self.cube[1] = np.rot90(self.cube[1], 3)
        temp = copy(self.cube[0][2])  # save up
        self.cube[0][2] = self.cube[4][:][2][::-1]  # write left into up
        for i in range(0, 3):
            self.cube[4][i][2] = self.cube[5][0][i]  # write down into left
        self.cube[5][0] = self.cube[2][:][0][::-1]  # write right into down
        for i in range(0, 3):
            self.cube[2][i][0] = temp[i]  # write up(temp) into right

    def print_cube(self):
        face_name = ["UP", "FRONT", "RIGHT", "BACK", "LEFT", "DOWN"]
        print("---------------CUBE---------------")
        for i in range(0, len(self.cube)):
            print(f"For {face_name[i]}-face the configuration is currently:")
            for j in range(0, len(self.cube[i])):
                print(self.cube[i][j])
        print("----------------------------------")
