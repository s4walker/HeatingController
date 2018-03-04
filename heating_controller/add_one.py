# -*- coding: utf-8 -*-
"""
Contains a function that takes in an argument, and adds one to it. This
describes a template for how code should be documented. Here's the breakdown

* The first line in a file is a comment indicating the text encoding used for
the Python file.
* If the file is executable, then add the shebang line
    ``#!/usr/bin/env python``. As a rule of thumb, if there is a
    :python:`if __name__ == '__main__':`` block, there should be a shebang
    line in the file.
* The next line is a triple-quoted string. This is a docstring that describes
    what the purpose of the module does
"""


def add_one(x):
    """
    Adds one to an argument. This triple-quoted string is an example of a
    function docstring. It describes what the function does on a user level.
    This docstring will get assigned to the variable ``add_one.__doc__``,
    which will make it available to documentation generators.

    :param int x: The number to which ``1`` should be added
    :return: The result of adding ``1`` to the argument
    """
    return x + 1
