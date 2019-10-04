import numpy as np
from src.model.maze.IMaze import IMaze


class Maze(IMaze):
    def __init__(self, cell_array=None, grid_shape=(10, 10)):
        super().__init__(cell_array, grid_shape)

    def to_string(self):
        string = ""
        for row in self.grid:
            for cell in row:
                string += cell.c_type + "-"
            string = string[:-1] + "\n"
        string = string[:-1]
        return string

