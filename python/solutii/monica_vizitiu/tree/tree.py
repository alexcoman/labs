#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=unused-argument

from __future__ import print_function
import os
import os.path

def tree(director,nivel):
     linii = "-"
     linii = linii * nivel 
     try:
        lista = os.listdir(director)
     except WindowsError: 
        return
     print(linii+director)
     for fis in lista:
        f = os.path.join(director,fis)
        if os.path.isfile(f)==True:
            print(linii+fis)
        elif os.path.isdir(f)==True:
            tree(f,nivel+1)
    

def main():
    """ Main function docstring """
    director = raw_input();
    tree(director,0)

if __name__ == "__main__":
    main()
