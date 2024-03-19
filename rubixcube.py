from copy import copy
import numpy as np
import random
# colors: Y(ellow),  O(range),   B(lue),     R(ed),     G(reen),    W(hite)
# faces:  0: UP,     1: FRONT,   2: RIGHT,   3: BACK,   4: LEFT,    5: DOWN


class RubixCube:
    def __init__(self, cube=None):
        if cube is None:
            cube = np.array([[["Y"] * 3] * 3, [["O"] * 3] * 3, [["B"] * 3] * 3, [["R"] * 3] * 3, [["G"] * 3] * 3,
                    [["W"] * 3] * 3])
        self.cube = cube
        self.moves = []

    def rotate_F(self):
        self.cube[1] = np.rot90(self.cube[1], 3)
        temp = np.copy(self.cube[0, 2])  # save up
        for i in range(0, 3):  # write left into up
            self.cube[0, 2, i] = self.cube[4, 2-i, 2]
        for i in range(0, 3):
            self.cube[4, i, 2] = self.cube[5, 0, i]  # write down into left
        for i in range(0, 3):  # write right into down
            self.cube[5, 0, i] = self.cube[2, 2-i, 0]
        for i in range(0, 3):
            self.cube[2, i, 0] = temp[i]  # write up(temp) into right
        self.moves.append("F")

    def rotate_R(self):
        self.cube[2] = np.rot90(self.cube[2], 3)
        temp = np.copy(self.cube[1, :, 2])  # save O
        for i in range(0, 3):
            self.cube[1, i, 2] = self.cube[5, i, 2]
        for i in range(0, 3):
            self.cube[5, i, 2] = self.cube[3, 2-i, 0]
        for i in range(0, 3):
            self.cube[3, i, 0] = self.cube[0, 2-i, 2]
        for i in range(0, 3):
            self.cube[0, i, 2] = temp[i]
        self.moves.append("R")

    def rotate_U(self):
        self.cube[0] = np.rot90(self.cube[0], 3)
        temp = np.copy(self.cube[3, 0])
        self.cube[3, 0] = np.copy(self.cube[4, 0])
        self.cube[4, 0] = np.copy(self.cube[1, 0])
        self.cube[1, 0] = np.copy(self.cube[2, 0])
        self.cube[2, 0] = temp
        self.moves.append("U")

    def rotate_L(self):
        self.cube[4] = np.rot90(self.cube[4], 3)
        temp = copy(self.cube[0, :, 0])
        for i in range(0, 3):
            self.cube[0, i, 0] = self.cube[3, 2-i, 2]
        for i in range(0, 3):
            self.cube[3, i, 2] = self.cube[5, 2-i, 0]
        for i in range(0, 3):
            self.cube[5, i, 0] = self.cube[1, i, 0]
        for i in range(0, 3):
            self.cube[1, i, 0] = temp[i]
        self.moves.append("L")

    def rotate_D(self):
        self.cube[5] = np.rot90(self.cube[5], 3)
        temp = np.copy(self.cube[1, 2])
        self.cube[1, 2] = np.copy(self.cube[4, 2])
        self.cube[4, 2] = np.copy(self.cube[3, 2])
        self.cube[3, 2] = np.copy(self.cube[2, 2])
        self.cube[2, 2] = temp
        self.moves.append("D")

    def rotate_F_prime(self):
        self.rotate_F()
        self.rotate_F()
        self.rotate_F()
        self.moves.append("F'")

    def rotate_R_prime(self):
        self.rotate_R()
        self.rotate_R()
        self.rotate_R()
        self.moves.append("R'")

    def rotate_U_prime(self):
        self.rotate_U()
        self.rotate_U()
        self.rotate_U()
        self.moves.append("U'")

    def rotate_L_prime(self):
        self.rotate_L()
        self.rotate_L()
        self.rotate_L()
        self.moves.append("L'")

    def rotate_D_prime(self):
        self.rotate_D()
        self.rotate_D()
        self.rotate_D()
        self.moves.append("D'")

    def is_cube_solved(self):
        possible_faces = ["Y", "O", "B", "R", "G", "W"]
        for face in self.cube:
            curr_color = face[0, 0]
            if curr_color not in possible_faces:
                return False
            possible_faces.remove(curr_color)
            for i in range(0, 3):
                for j in range(0, 3):
                    if curr_color != face[i, j]:
                        return False
        return True

    def scramble_from_text_input(self, input="F2 R F' F"):
        scrambles = input.strip().split(" ")
        kind_to_rotate = {"F": self.rotate_F,
                          "R": self.rotate_R,
                          "U": self.rotate_U,
                          "L": self.rotate_L,
                          "D": self.rotate_D,
                          "F'": self.rotate_F_prime,
                          "R'": self.rotate_R_prime,
                          "U'": self.rotate_U_prime,
                          "L'": self.rotate_L_prime,
                          "D'": self.rotate_D_prime}
        for scramble in scrambles:
            kind = scramble[0]
            amount = 1
            if len(scramble) == 2:
                if scramble[1] == "'":
                    kind = scramble
                else:
                    amount = int(scramble[1])
            for i in range(amount):
                kind_to_rotate[kind]()

    def scramble_cube_randomly(self, num_of_scrambles=20):
        funcs = [self.rotate_F, self.rotate_R, self.rotate_U, self.rotate_L, self.rotate_D,
                 self.rotate_F_prime, self.rotate_R_prime, self.rotate_U_prime, self.rotate_L_prime, self.rotate_D_prime]
        for i in range(0, num_of_scrambles):
            func_index = random.randint(0, 9)
            funcs[func_index]()

    def print_cube(self):
        face_name = ["UP", "FRONT", "RIGHT", "BACK", "LEFT", "DOWN"]
        print("---------------CUBE---------------")
        for i in range(0, len(self.cube)):
            print(f"For {face_name[i]}-face the configuration is currently:")
            for j in range(0, len(self.cube[i])):
                print(self.cube[i, j])
        print("----------------------------------")

    def print_face(self, face=0):
        print("---------------FACE---------------")
        print("----------------" + str(face) + "-----------------")
        above = self.cube[3, 0][::-1]
        below = self.cube[1, 0]
        left = self.cube[4, 0]
        right = self.cube[2, 0][::-1]
        if face == 1:
            above = self.cube[0, 2]
            below = self.cube[5, 0]
            left = self.cube[4, :, 2]
            right = self.cube[2, :, 0]
        elif face == 2:
            above = self.cube[0, :, 2][::-1]
            below = self.cube[5, :, 2]
            left = self.cube[1, :, 2]
            right = self.cube[3, :, 0]
        elif face == 3:
            above = self.cube[0, 0][::-1]
            below = self.cube[5, 2][::-1]
            left = self.cube[2, :, 0]
            right = self.cube[4, :, 0]
        elif face == 4:
            above = self.cube[0, :, 0]
            below = self.cube[5, :, 0][::-1]
            left = self.cube[3, :, 2]
            right = self.cube[1, :, 0]
        elif face == 5:
            above = self.cube[1, 2]
            below = self.cube[3, 2][::-1]
            left = self.cube[4, 2][::-1]
            right = self.cube[2, 2]
        print("   " + str(above))
        for i in range(0, 3):
            print(str(left[i]) + str(self.cube[face, i]) + str(right[i]))
        print("   " + str(below))
        print("----------------------------------")

    def status_report(self):
        print("---------------INFO---------------")
        print("The cube was rotated", len(self.moves), "times.")
        print("Rotations were", self.moves)
        self.print_cube()
        print("----------------------------------")