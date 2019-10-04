import pytest
from src.model.maze.Maze import Maze
from src.model.maze.MockMaze import MockMaze


def test_mock_impl():
    maze = MockMaze()
    assert maze is not None


def test_empty_constructor():
    maze = Maze()
    # think about what to do 



