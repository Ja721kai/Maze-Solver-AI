import pytest
from src.model.agent.Agent import Agent
from src.model.agent.MockAgent import MockAgent


def test_mock_impl():
    agent = MockAgent()
    assert agent is not None


def test_mock_impl2():
    agent = MockAgent()
    assert agent.get_map() == []


def test_mock_impl3():
    agent = MockAgent()
    assert agent.get_policy() == []


def test_mock_impl4():
    agent = MockAgent()
    assert agent.get_reward_table() == []


def test_mock_impl5():
    agent = MockAgent()
    assert agent.get_state() is None


def test_mock_impl6():
    agent = MockAgent()
    assert agent.get_value_table() == []


def test_set_state():
    agent = Agent()
    state = 5
    agent.set_state(state)
    assert agent.get_state() == state
