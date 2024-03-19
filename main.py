import rubixcube
import numpy as np
import pygame
import itertools as it



def game_demo():
    pygame.init()
    pygame.display.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((512, 512))
    canvas = pygame.Surface((512, 512))
    canvas.fill((128, 128, 128))
    pix_square_size = (
            512 / 16
    )

    colors = {"W": (255, 255, 255), "Y": (255, 255, 0), "R": (255, 0, 0), "G": (0, 255, 0), "B": (0, 0, 255),
              "O": (255, 128, 0)}
    face_offsets = {0: [3, 0], 1: [3, 3], 2: [6, 3], 3: [9, 3], 4: [0, 3], 5: [3, 6]}
    general_offset = [2, 4]

    for face in range(len(c)):
        face_offset = face_offsets[face]
        for i in range(3):
            for j in range(3):
                color = colors[c[face, i, j]]
                pygame.draw.rect(
                    canvas,
                    color,
                    pygame.Rect(
                        pix_square_size * np.array(
                            [i + face_offset[0] + general_offset[0], j + face_offset[1] + general_offset[1]]),
                        (pix_square_size, pix_square_size),
                    ),
                )

    for i in range(7, 11):
        pygame.draw.line(
            canvas,
            0,
            (64, pix_square_size * i),
            (448, pix_square_size * i),
            width=3,
        )

    for i in it.chain(range(4, 7), range(11, 14)):
        pygame.draw.line(
            canvas,
            0,
            (160, pix_square_size * i),
            (256, pix_square_size * i),
            width=3,
        )

    for i in range(5, 9):
        pygame.draw.line(
            canvas,
            0,
            (pix_square_size * i, 128),
            (pix_square_size * i, 416),
            width=3,
        )

    for i in it.chain(range(2, 5), range(9, 15)):
        pygame.draw.line(
            canvas,
            0,
            (pix_square_size * i, 224),
            (pix_square_size * i, 320),
            width=3,
        )

    for i in range(30):
        window.blit(canvas, canvas.get_rect())
        pygame.event.pump()
        pygame.display.update()
        clock.tick(4)


if __name__ == '__main__':
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

    c = np.array([[["Y"] * 3] * 3,
                  [["O"] * 3] * 3,
                  [["B"] * 3] * 3,
                  [["R"] * 3] * 3,
                  [["G"] * 3] * 3,
                  [["W"] * 3] * 3])

    cube = rubixcube.RubixCube(c)




