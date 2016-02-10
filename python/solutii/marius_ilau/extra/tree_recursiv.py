""" Missed module docstring docstring """
from __future__ import print_function
import os


def tree_recursiv(cale):
    """ Tree recursiv """
    fis = os.listdir(cale)
    print("Directoare din " + cale + " :")
    for item in fis:
        cale2 = os.path.join(cale, item)
        if os.path.isdir(cale2):
            print(cale2 + ":")
            tree_recursiv(cale2)
        elif os.path.isfile(cale2):
            print(cale2)

if __name__ == "__main__":
    tree_recursiv("/Users/ilaumarius")
