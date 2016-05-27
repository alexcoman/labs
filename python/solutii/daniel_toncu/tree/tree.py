"""
Acest modul afiseaza la iesirea standard arborele pentru ierarhia de
directoare, pornind de la un director - identificat print path - dat ca
parametru la linia de comanda.
Similar comenzii tree din Linux.
"""

import sys
import os
import os.path

INDENTATION_DIM = '   '


def print_tree(dirpath, indentation):

    """
    Parcurge directorul ce se gaseste la path-ul dirpath si afiseaza
    numele tuturor instantelor din el. Toate directoarele ce se gasesc in
    directorul curent, sunt parcurse recursiv.
    Note: Fisierele sunt precedate de [F], Directoarele sunt precedate de
    [D], si intrarile necunoscute sunt precedate de [U].
    """

    new_indentation = indentation + INDENTATION_DIM
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isfile(filepath):
            print new_indentation + '[F] ' + filename
        elif os.path.isdir(filepath):
            print new_indentation + '[D] ' + filename
            print_tree(filepath, new_indentation)
        else:
            print new_indentation + '[U] ' + filename

if __name__ == "__main__":
    print
    if len(sys.argv) != 2:
        print "Prea putine/multe argumente!"
        print " Usage: python {} <dirpath>".format(sys.argv[0])
    elif not os.path.isdir(os.path.join(sys.argv[1])):
        print "{} nu este un director!".format(sys.argv[1])
    else:
        print " {}'s Tree:\n".format(sys.argv[1])
        print_tree(sys.argv[1], ' ')
