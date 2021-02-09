#!/usr/bin/env python3

"""
Install snake package
"""

from setuptools import setup

setup(
    name="snake",
    version="0.0.1",
    entry_points={
        "console_scripts": ["snake = snake.__main__:run_program"]
    }
)