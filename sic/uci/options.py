# -*- coding: utf-8 -*-
"""
UCI options

Support for UCI options
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
from __future__ import annotations

from typing import Any, Callable, Type, TypeAlias, TypeVar, Union

ButtonType: TypeAlias = Callable[[], Any]


class Combo:
    """UCI combobox."""

    def __init__(self, possible_values: list[str], default_value: str) -> None:
        """
        Initialize combobox.

        :param list[str] possible_values: Possible values.
        :param str default_value: Default value.
        """
        self.possible_values: list[str] = possible_values
        self.value: str = default_value

    def __str__(self) -> str:
        """
        Get value as a string.

        :return str: Value.
        """
        return self.value


class Button:
    """UCI button."""

    def __init__(self, function: ButtonType) -> None:
        """
        Initialize button.

        :param ButtonType function: Function to call.
        """
        self.function: ButtonType = function


class Spin:
    """UCI spin."""

    def __init__(self, maximum: int, minimum: int, value: int) -> None:
        """
        Initialize spin.

        :param int maximum: Maximum value.
        :param int minimum: Minimum value.
        :param int value: Value.
        """
        self.range: tuple[int, int] = (minimum, maximum)
        self.value: int = value

    def __str__(self) -> str:
        """
        Get value as a string.

        :return str: Value.
        """
        return str(self.value)


T = TypeVar("T", bool, Spin, Button, Combo, str)
OptionInfos: TypeAlias = tuple[str, str, list[tuple[str, str]]]
AllTypes: TypeAlias = Union[bool, Spin, Button, Combo, str]

TYPES_ALIASES: dict[Type[AllTypes], str] = {
    bool: "check",
    Spin: "spin",
    Button: "button",
    Combo: "combo",
    str: "string",
}


class Option:
    """An UCI option."""

    def __init__(self, name: str, value: T) -> None:
        """
        Initialize an option.

        :param str name: Option name.
        :param T value: Value.
        """
        self.name: str = name
        self.value: AllTypes = value
        self.default: AllTypes = value

    def get_option(self) -> OptionInfos:
        """
        Get this option informations.

        :return OptionInfos: Options for UCI.
        """
        params: list[tuple[str, str]] = []
        if not isinstance(self.value, Button):
            if type(self.value) in (bool, str, Combo, Spin):
                params = [("default", str(self.default))]
            if isinstance(self.value, Combo):
                for val in self.value.possible_values:
                    params.append(("val", val))
            if isinstance(self.value, Spin):
                params.extend(
                    (
                        ("min", str(self.value.range[0])),
                        ("max", str(self.value.range[1])),
                    )
                )
        result: OptionInfos = (self.name, TYPES_ALIASES[type(self.value)], params)
        return result
