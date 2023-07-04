#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Launcher

Launches the CLI
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

from . import cli

if __name__ == "__main__":
    print(
        """SIC - SImple Chess Engine  Copyright (C) 2023  Virinas-code
This program comes with ABSOLUTELY NO WARRANTY; for details type 'sic:license w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'sic:license c' for details."""
    )
    cli()
