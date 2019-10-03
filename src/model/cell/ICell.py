import numpy as np

# abstract base class for interface implementation
import abc


class ICell(abc.ABC):

    allowed_types = ['X', '_']

    def __init__(self, c_type='X'):
        assert c_type in self.allowed_types, "Given Cell Type does not exist"
        self.c_type = c_type

    def _type(self):
        return self.c_type

    def get_allowed_types(self):
        return self.allowed_types
