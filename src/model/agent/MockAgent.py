import numpy as np
from src.model.agent.IAgent import IAgent


class MockAgent(IAgent):
    def __init__(self):
        super().__init__()
