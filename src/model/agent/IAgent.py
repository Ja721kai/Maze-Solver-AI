import numpy as np

# abstract base class for interface implementation
import abc


class IAgent(abc.ABC):

    maze_map = []
    state = None
    V = []
    R = []
    policy = []

    def __init__(self):
        pass

    def get_map(self):
        return self.maze_map

    def get_state(self):
        return self.state

    def get_value_table(self):
        return self.V

    def get_reward_table(self):
        return self.R

    def get_policy(self):
        return self.policy
