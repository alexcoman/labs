"""
    cauta recursiv in directorul dat de path fisierele cu nume
    ce contine a sau A
"""
import os
import sys


def cauta(path):
    """cauta recursiv fisierele ce contin a sau A in nume"""
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            if "a" in name.lower():
                print os.path.join(path, name)
        if os.path.isdir(os.path.join(path, name)):
            cauta(os.path.join(path, name))


if __name__ == "__main__":
    cauta(sys.argv[1])
