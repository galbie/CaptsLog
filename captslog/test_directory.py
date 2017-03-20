# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from example_google import *

import pytest


def square(x):
    """Example function with types documented in the docstring.

    Args:
        x (int): The first parameter.

    Returns:
        int: Square value of x

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    return x ** 2


def test_square():
    """Test Square.

    For test functionality of pytest

    """
    x = [1, 2, 3, 4, 5]
    x_square = [1, 4, 9, 16, 25]

    for ind, y in enumerate(x):
        assert x_square[ind] == square(y)
