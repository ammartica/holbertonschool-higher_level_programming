#!/usr/bin/python3
"""
Contains read_file function
"""


def read_file(filename=""):
    """""reads and prints text file(UTF8)"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
