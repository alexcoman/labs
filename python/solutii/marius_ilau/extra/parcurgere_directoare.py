""" Parcurgere recursiva prin director - extra """
from __future__ import print_function
import os


def parcurgere_directoare(start_path, mesaj):
    """ Parcurgere recursiva prin director """
    for item in os.listdir(start_path):
        path = os.path.join(start_path, item)
        if os.path.isfile(path):
            fis = open(path, "r")
            for line in fis:
                if mesaj in line:
                    print(item)
        if os.path.isdir(path):
            parcurgere_directoare(path, mesaj)

if __name__ == "__main__":
    parcurgere_directoare("/Users/ilaumarius", "gg")
