import rubixcube
import gymnasium as gym
from gymnasium import spaces
import pygame
import numpy as np
import itertools as it


class RubixCubeEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5):
        self.cube = rubixcube.RubixCube()
        self.window_size = 512  # The size of the PyGame window

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        # TODO: observation space needs good observations
        self.observation_space = spaces.Dict(
            {
                "cube": spaces.Box(0, 5, shape=(6, 3, 3), dtype=np.integer),
            }
        )

        # We have 4 actions, corresponding to "right", "up", "left", "down"
        self.action_space = spaces.Discrete(10)

        """
        The following dictionary maps abstract actions from `self.action_space` to
        the direction we will walk in if that action is taken.
        I.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_rotation = {
            0: self.cube.rotate_F,
            1: self.cube.rotate_R,
            2: self.cube.rotate_U,
            3: self.cube.rotate_L,
            4: self.cube.rotate_D,
            5: self.cube.rotate_F_prime,
            6: self.cube.rotate_R_prime,
            7: self.cube.rotate_U_prime,
            8: self.cube.rotate_L_prime,
            9: self.cube.rotate_D_prime,
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None


    def convert_array_to_num(self):
        letter_to_number = {"W": 5, "Y": 0, "R": 3, "G": 4, "B": 2, "O": 1}
        num_array = np.zeros(self.cube.cube.shape)
        for f in range(self.cube.cube):
            for i in range(3):
                for j in range(3):
                    num_array[f, i, j] = letter_to_number[self.cube.cube[f, i, j]]
        return num_array

    def _get_obs(self):
        return {"cube": self.convert_array_to_num()}

    def _get_info(self):
        return {"solved": self.cube.is_cube_solved()}

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self.cube.reset_cube()
        self.cube.scramble_cube_randomly()

        observation = self._get_obs()
        info = self._get_info()

        self._render_frame()

        return observation, info

    def step(self, action):
        rotation = self._action_to_rotation[action]
        rotation()
        terminated = self.cube.is_cube_solved()
        reward = 1 if terminated else 0
        observation = self._get_obs()
        info = self._get_info()

        self._render_frame()

        return observation, reward, terminated, False, info

    def _render_frame(self):
        if self.window is None:
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode(
                (self.window_size, self.window_size)
            )
        if self.clock is None:
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((128, 128, 128))
        pix_square_size = (
                self.window_size / 16
        )  # The size of a single grid square in pixels

        colors = {"W": (255, 255, 255), "Y": (255, 255, 0), "R": (255, 0, 0), "G": (0, 255, 0), "B": (0, 0, 255),
                  "O": (255, 128, 0)}
        face_offsets = {0: [3, 0], 1: [3, 3], 2: [6, 3], 3: [9, 3], 4: [0, 3], 5: [3, 6]}
        general_offset = [2, 4]

        for face in range(len(self.cube.cube)):
            face_offset = face_offsets[face]
            for i in range(3):
                for j in range(3):
                    color = colors[self.cube.cube[face, i, j]]
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

        self.window.blit(canvas, canvas.get_rect())
        pygame.event.pump()
        pygame.display.update()

        self.clock.tick(self.metadata["render_fps"])

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
