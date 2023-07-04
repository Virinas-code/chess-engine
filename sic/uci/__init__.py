# -*- coding: utf-8 -*-
"""
UCI Interface

Main class
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
