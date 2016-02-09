"""
Iterate through all folders to find files containing
a given letter
"""
from __future__ import print_function
import os


def find_allfiles(mdirectory, char):
    """
    Prints out all the files
    :param mdirectory: the main directory
    :param char: the char we are looking for
    :return: to the console all the files
    """
    for cfile in os.listdir(mdirectory):
        if os.path.isdir(os.path.join(mdirectory, cfile)):
            find_allfiles(os.path.join(mdirectory, cfile), char)
        else:
            if char in cfile:
                print(os.path.abspath(cfile))


if __name__ == "__main__":
    find_allfiles("C:\\", "a")
