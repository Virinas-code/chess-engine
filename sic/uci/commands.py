# -*- coding: utf-8 -*-
"""
UCI commands

Handles inputs
"""
from typing import Callable, Final

SUPPORTED_KEYWORDS: Final[list[str]] = ["id"]


class Commands:
    """UCI commands"""

    def __init__(self, version: str, author: str) -> None:
        """
        Initializes interface.

        :param str version: Version.
        :param str author: Author.
        """
        self.version: Final[str] = version
        self.author: Final[str] = author
        self.keywords: dict[str, Callable[[list[str]], None]] = {
            "id": self.uci_id,
        }

    def run(self, prompt: str) -> None:
        """
        Run a command.

        :param str prompt: User input.
        """
        parsed: list[str] = prompt.split()
        for index, command in enumerate(parsed):
            if command in self.keywords:
                params_index: int = index + 1
                self.keywords[command](parsed[params_index:])

    def uci_id(self, params: list[str]) -> None:
        """
        UCI ``id`` command.

        :param list[str] params: Arguments.
        """
        print("id", "name", f"SIC - SImple Chess engine v{self.version}")
        print("id", "author", self.author)
