import numpy as np
from src.model.cell.ICell import ICell


class Cell(ICell):
    def __init__(self, c_type=None):
        if c_type is not None:
            super().__init__(c_type)
        else:
            super().__init__()
