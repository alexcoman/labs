"""
Represent a directory as a tree
"""

from __future__ import print_function
import os


def rtree(mdirectory, depth):
    """
    Display a tree
    :param mdirectory: the main directory
    :param depth: the depth from where we start
    :return: prints the whole tree
    """
    files_in_dir = os.listdir(mdirectory)
    print('\t' * depth, os.path.basename(mdirectory))
    for cfile in files_in_dir:
        if os.path.isdir(os.path.join(mdirectory, cfile)):
            rtree(os.path.join(mdirectory, cfile), depth+1)
        else:
            print('\t' * (depth+1), os.path.basename(cfile))


if __name__ == "__main__":
    rtree("C:", 0)
