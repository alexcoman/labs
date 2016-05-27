#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Problema Paranteze."""

from __future__ import print_function


def verifica_expresia(paranteze):
    """verificare"""
    lista = []
    for paranteza in paranteze:
        if paranteza == '(' or paranteza == '[':
            lista.append(paranteza)
        else:
            if len(lista) > 0:
                xelement = lista.pop()
                if paranteza == ']' and xelement != '[':
                    return False
                elif paranteza == ')' and xelement != '(':
                    return False
            else:
                return False
    return True


if __name__ == "__main__":
    assert verifica_expresia("[()[]]"), "Probleme la expresia 1"
    assert verifica_expresia("()()[][]"), "Probleme la expresia 2"
    assert verifica_expresia("([([])])"), "Probleme la expresia 3"
    assert not verifica_expresia("[)()()()"), "Probleme la expresia 4"
    assert not verifica_expresia("][[()][]"), "Probleme la expresia 5"
    assert not verifica_expresia("([()]))"), "Probleme la expresia 6"
    assert not verifica_expresia("([)]"), "Probleme la expresia 7"
