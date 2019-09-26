import numpy as np
from src.model.cell.ICell import ICell


class MockCell(ICell):
    def __init__(self):
        super().__init__()

    def _type(self):
        return super()._type()
