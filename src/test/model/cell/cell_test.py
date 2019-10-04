import pytest
from src.model.cell.Cell import Cell
from src.model.cell.MockCell import MockCell


def test_non_existent_constructor_parameter():
    with pytest.raises(AssertionError):
        Cell(c_type='x')


def test_no_constructor_given():
    cell = Cell()
    assert cell._type() == 'X'


def test_no_constructor_given2():
    cell = Cell(c_type=None)
    assert cell._type() == 'X'


def test_with_correct_type1():
    cell = Cell(c_type='X')
    assert cell._type() == 'X'


def test_with_correct_type2():
    cell = Cell(c_type='_')
    assert cell._type() == '_'


def test_available_types():
    cell = Cell()
    types = cell.get_allowed_types()
    for type in types:
        cell = Cell(c_type=type)
        assert cell._type() == type

        
def test_mock_impl():
    cell = MockCell()
    assert cell is not None
