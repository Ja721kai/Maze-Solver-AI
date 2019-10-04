import pytest
import numpy as np
from src.model.cell.Cell import Cell
from src.model.maze.Maze import Maze
from src.model.maze.MockMaze import MockMaze


def test_mock_impl():
    maze = MockMaze()
    assert maze is not None


def test_mock_impl2():
    maze = MockMaze()
    assert maze.to_string() == ""


def test_empty_constructor():
    maze = Maze()
    assert np.shape(maze.grid) == (10, 10)  # decided on (10, 10) to be standard maze size


def test_constructing_with_cellarray():
    wall = Cell('X')
    ground = Cell('_')
    cell_array = np.array([[wall, wall, wall],
                           [ground, ground, ground],
                           [wall, wall, wall]])
    maze = Maze(cell_array=cell_array)
    assert maze.grid.all() == cell_array.all()


def test_constructing_with_wrong_gridshape():
    with pytest.raises(AssertionError):
        Maze(grid_shape=(5, 5, 4))


def test_constructing_with_wrong_gridshape2():
    with pytest.raises(TypeError):
        Maze(grid_shape=5)


def test_constructing_with_wrong_gridshape3():
    with pytest.raises(AssertionError):
        Maze(grid_shape=(5,))


def test_to_string():
    wall = Cell('X')
    ground = Cell('_')
    cell_array = np.array([[wall, wall, wall],
                           [ground, ground, ground],
                           [wall, wall, wall]])
    maze = Maze(cell_array=cell_array)
    maze_string = maze.to_string()
    assert maze_string == "X-X-X\n_-_-_\nX-X-X"


def test_to_string2():
    maze = Maze()
    maze_string = maze.to_string()
    assert maze_string == (("X-" * 9 + "X\n") * 10)[:-1]

