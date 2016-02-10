#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Scrieți o funcție ce să determine dacă numărul primit
ca argument este o putere a lui 2.
"""


def putere_eficient(numar):
    """Functie ce determina daca un numar este putere a lui 2."""
    return (numar & numar - 1) == 0


def putere(numar):
    """Funcție ce determină dacă un număr este putere a lui 2."""
    numar_binar = "{0:b}".format(numar)
    return numar_binar.count("1") == 1


if __name__ == "__main__":
    assert putere(2)
    assert putere(4)
    assert not putere(10)
