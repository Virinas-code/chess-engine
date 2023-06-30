# -*- coding: utf-8 -*-
"""
Main CLI

Used to start engine
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

from importlib.metadata import PackageMetadata, metadata
from typing import Final

import click

from .uci import UCI

sic: PackageMetadata = metadata("sic")
__version__: Final[str] = sic["Version"]
__author__: Final[str] = sic["Author"]


@click.group()
def cli() -> None:
    """
    Welcome to SIC - SImple Chess engine!

    SIC is a simple chess engine created as an amateur project
    by Virinas-code.

    It is just an empty project for now, but I'm going
    to make it a fully working chess engine!
    """
    pass


@cli.command()
def uci() -> None:
    """Start UCI prompt."""
    uci: UCI = UCI(__version__, __author__)
    return uci.start()
