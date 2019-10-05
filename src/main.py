from src.view.tui import Tui
from src.view.tui import Gui
from src.model.maze.Maze import Maze
from src.model.agent.Agent import Agent
from src.controller.environment import Environment

import logging
from threading import Thread
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(str(__name__).split(".")[-1].upper().strip("_"))


if __name__ == '__main__':
    # tui_thread = Thread(target=Tui, args=(logging.INFO,))
    # tui_thread.start()
    tui = Tui()
    gui = Gui()
    agent = Agent()
    maze = Maze()
    controller = Environment()

    tui.add_controller(controller)
    gui.add_controller(controller)
    agent.add_view(tui, gui)
    controller.add_model(agent, maze)
    controller.add_view(tui, gui)
    while 1:
        pass


