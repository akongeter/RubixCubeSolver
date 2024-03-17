import unittest
import numpy as np
import rubixcube


class MyTestCase(unittest.TestCase):

    def assert_same_cube(self, a, b, face="No relevant face selected"):
        for x in range(len(a)):
            for y in range(len(a[0])):
                for z in range(len(a[0, 0])):
                    self.assertEqual(a[x, y, z], b[x, y, z], face)

    def get_unscrambled_cube(self):
        a = np.array([[["Y00", "Y01", "Y02"],
                       ["Y10", "Y11", "Y12"],
                       ["Y20", "Y21", "Y22"]],

                      [["O00", "O01", "O02"],
                       ["O10", "O11", "O12"],
                       ["O20", "O21", "O22"]],

                      [["B00", "B01", "B02"],
                       ["B10", "B11", "B12"],
                       ["B20", "B21", "B22"]],

                      [["R00", "R01", "R02"],
                       ["R10", "R11", "R12"],
                       ["R20", "R21", "R22"]],

                      [["G00", "G01", "G02"],
                       ["G10", "G11", "G12"],
                       ["G20", "G21", "G22"]],

                      [["W00", "W01", "W02"],
                       ["W10", "W11", "W12"],
                       ["W20", "W21", "W22"]]])
        return np.copy(a)

    def test_rotate_F(self):
        print("------Starting rotate_F Test------")
        a = self.get_unscrambled_cube()

        b = np.copy(a)
        cube = rubixcube.RubixCube(a)
        for i in range(0, 4):
            cube.rotate_F()
        self.assert_same_cube(a, b, cube.print_face(1))

    def test_rotate_R(self):
        print("------Starting rotate_R Test------")
        a = self.get_unscrambled_cube()

        b = np.copy(a)
        cube = rubixcube.RubixCube(a)
        for i in range(0, 4):
            cube.rotate_R()
        self.assert_same_cube(a, b, cube.print_face(2))

    def test_rotate_U(self):
        print("------Starting rotate_U Test------")
        a = self.get_unscrambled_cube()

        b = np.copy(a)
        cube = rubixcube.RubixCube(a)
        for i in range(0, 4):
            cube.rotate_U()
        self.assert_same_cube(a, b, cube.print_face(0))

    def test_rotate_L(self):
        print("------Starting rotate_L Test------")
        a = self.get_unscrambled_cube()

        b = np.copy(a)
        cube = rubixcube.RubixCube(a)
        for i in range(0, 4):
            cube.rotate_L()
        self.assert_same_cube(a, b, cube.print_face(4))

    def test_rotate_D(self):
        print("------Starting rotate_D Test------")
        a = self.get_unscrambled_cube()

        b = np.copy(a)
        cube = rubixcube.RubixCube(a)
        for i in range(0, 4):
            cube.rotate_D()
        self.assert_same_cube(a, b, cube.print_face(5))



if __name__ == '__main__':
    unittest.main()
