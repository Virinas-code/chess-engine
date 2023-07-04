# -*- coding: utf-8 -*-
"""
UCI commands

Handles inputs
"""
# SIC - SImple Chess engine
# Copyright (C) 2023  Virinas-code
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# A copy of the GNU General Public License can be found in the file
# LICENSE

import sys
from multiprocessing.shared_memory import ShareableList
from typing import Callable, Final

from .options import Option, OptionInfos, Spin

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
            "uci": self.uci,
            "quit": self.quit,
        }
        self.options: dict[str, Option] = {
            "Hash": Option("Hash", Spin(32768, 4, 64)),
            "MultiPV": Option("MultiPV", Spin(64, 1, 1)),
        }
        self.shared_queue: ShareableList = ShareableList([], name="sic_uci_queue")

    def _display_options(self) -> None:
        """
        Display options.

        See options.py.
        """
        for option in self.options.values():
            infos: OptionInfos = option.get_option()
            details: list[str] = []
            for data in infos[2]:
                details.extend((data[0], data[1]))
            print("option", "name", infos[0], "type", infos[1], string)

    def _process(self) -> None:
        """
        Process inputs.

        Used for multithreading.
        """
        shared_object: ShareableList = ShareableList(name="sic_uci_queue")
        while True:
            if len(shared_object) > 0:
                print(shared_object[-1])

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
                break

    def uci(self, _: list[str]) -> None:
        """
        UCI ``uci`` command.

        :param list[str] _: Arguments.
        """
        self.uci_id()
        self._display_options()
        self.uciok()

    @staticmethod
    def quit(_: list[str]) -> None:
        """
        UCI ``quit`` command.

        :param list[str] _: Arguments.
        """
        # TODO: Add engine stop
        sys.exit(0)

    def uci_id(self) -> None:
        """
        UCI ``id`` command.

        Displays engine informations.
        """
        print("id", "name", f"SIC - SImple Chess engine v{self.version}")
        print("id", "author", self.author)

    @staticmethod
    def uciok() -> None:
        """
        UCI ``uciok`` command.

        Tells the GUI the engine is on UCI.
        """
        print("uciok")
