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
