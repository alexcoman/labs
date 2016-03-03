"""
Fisier de configurare
"""

from __future__ import print_function


PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

IGNORE_FILES = ['.', '..', '.idea', '.git']


def help_function(name, options):
    """Metoda afiseaza un mesaj de ajutor
    in cazul in care datele introduse sunt gresite
    """
    print('{0}NAME{1}'.format(BOLD, END))
    print('\t {0}\n'.format(name))
    print('{0}SYNOPSIS{1}'.format(BOLD, END))
    print('\t python {0}{1}{2} [OPTIONS] PATTERN [FILE...]\n'
          .format(BOLD, name, END))
    print('{0}DESCRIPTION{1}'.format(BOLD, END))
    print('\t {0}{1}{2} searches the named input {3}FILE{4}s '
          'for lines containing a match to the given {5}PATTERN{6}\n'
          .format(BOLD, name, END, UNDERLINE,
                  END, UNDERLINE, END))
    print('{0}OPTIONS{1}'.format(BOLD, END))
    for key, value in options.iteritems():
        print('\t {0}{1}{2} {3}\t'
              .format(BOLD, key, END, value))
    print('{0}EXAMPLE{1}'.format(BOLD, END))
    print('\t python {0}{1}{2} -in "CARD" teoreme1.txt'
          .format(BOLD, name, END))
