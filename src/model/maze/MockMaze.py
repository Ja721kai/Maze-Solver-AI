import numpy as np
from src.model.maze.IMaze import IMaze


class MockMaze(IMaze):
    def __init__(self):
        super().__init__()

    def to_string(self):
        return super().to_string()
