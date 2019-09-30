import unittest
from src.model.cell.Cell import Cell


class CellTest(unittest.TestCase):

    def test_wrong_constructor_parameter(self):
        with self.assertRaises(AssertionError):
            Cell('x')

    def test_no_constructor_given(self):
        cell = Cell()
        self.assertEqual(cell._type(), 'X')

    def test_no_constructor_given2(self):
        cell = Cell(None)
        self.assertEqual(cell._type(), 'X')


def test():
    unittest.main(verbosity=2)
