import pytest
from src.model.cell.Cell import Cell


def test_wrong_constructor_parameter():
    with pytest.raises(AssertionError):
        Cell('x')


def test_no_constructor_given():
    cell = Cell()
    assert cell._type() == 'X'


def test_no_constructor_given2():
    cell = Cell(None)
    assert cell._type() == 'X'
