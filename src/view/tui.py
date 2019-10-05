import logging


class Tui:
    def __init__(self, debug_level=logging.INFO):
        self.logger = logging.getLogger(__name__.split(".")[-1].upper())
        self.logger.setLevel(debug_level)

        self.logger.info("TUI instantiated.")

