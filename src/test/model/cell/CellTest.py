import unittest
from src.model.cell.Cell import Cell


class CellTest(unittest.TestCase):

    def test_wrong_constructor_parameter(self):
        with self.assertRaises(AssertionError):
            Cell('x')

    def test_no_constructor_given(self):
        cell = Cell()

    def test_no_constructor_given2(self):
        Cell(None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
