# -*- coding: utf-8 -*-
"""
UCI Interface

Main class
"""
from .commands import Commands


class UCI:
    """UCI interface."""

    def __init__(self, version: str, author: str) -> None:
        """
        Initialize interface.

        :param str version: Version.
        :param str author: Author.
        """
        self.commands: Commands = Commands(version, author)

    def start(self) -> None:
        """
        Starts UCI.

        Prints ID and starts main loop.
        """
        self.commands.uci_id()
        self.main_loop()

    def main_loop(self) -> None:
        """
        Starts UCI main loop.

        Asks for input and runs it.
        """
        while True:
            prompt: str = input()
            self.commands.run(prompt)
