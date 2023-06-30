# -*- coding: utf-8 -*-
"""
Main CLI

Used to start engine
"""
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
