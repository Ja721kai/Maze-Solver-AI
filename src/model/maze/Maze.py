import numpy as np
from src.model.maze.IMaze import IMaze


class Maze(IMaze):
    def __init__(self, cell_array=None, grid_shape=(10, 10)):
        super().__init__(cell_array, grid_shape)
