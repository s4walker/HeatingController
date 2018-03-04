#!/usr/bin/env python
"""
Contains instructions to pip on what this project is and how to install it.
The ``install_requires`` keyword argument sent to the setup function should
contain the minimum dependencies required to run the application. The
``requirements.txt`` contains the minimum dependencies required to develop the
application.
"""

from setuptools import setup, find_packages

setup(
    name='heating_controller',
    version='0.1',
    description='Heating controller for an STM setup',
    author='Sean Walker',
    author_email='s4walker@uwaterloo.ca',
    packages=find_packages(exclude=['test.*']),
    install_requires=[]
)
