import numpy as np

# abstract base class for interface implementation
import abc

from src.model.cell.Cell import Cell


class IMaze(abc.ABC):
    def __init__(self, cell_array=None, grid_shape=(10, 10)):
        if type(grid_shape) is not tuple:
            raise TypeError
        assert len(grid_shape) == 2
        if cell_array is None:
            self.grid = np.full(grid_shape, Cell())
            self.grid_shape = grid_shape
        else:
            self.grid = cell_array
            self.grid_shape = np.shape(cell_array)

    @abc.abstractmethod
    def to_string(self):
        return ""
