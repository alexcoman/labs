""" Acest script creeaza un tree walk pentru un folder dar ca parametru.
Output-ul este similar cu cel al comenzii 'tree'  din Linux."""

import os
import tkFileDialog


def list_files(locatie):
    """ Functia care creeaza tree-ul   """
    for root, dirs, files in os.walk(locatie):
        for directoare in dirs:
            print "Subfoldere : %s " % directoare
        nivel = root.replace(locatie, '').count(os.sep)
        spatiu = '-' * 4 * (nivel)
        print '[DIR ]|%s%s' % (spatiu, os.path.basename(root))
        spatiu2 = '-' * 4 * (nivel + 1)
        for fisier in files:
            print '[FILE]|%s%s' % (spatiu2, fisier)

if __name__ == "__main__":
    list_files(tkFileDialog.askdirectory())
