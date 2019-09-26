import numpy as np
from src.model.cell.ICell import ICell


class Cell(ICell):
    def __init__(self, type):
        super().__init__(type)
