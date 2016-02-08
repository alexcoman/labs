#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Tuxy scrie în fiecare zi foarte multe formule matematice.

Pentru că formulele sunt din ce în ce mai complicate trebuie
să folosească o serie de paranteze și a descoperit că cea
mai frecventă problemă a lui este că nu toate parantezele
sunt folosite cum trebuie.

Pentru acest lucru a apelat la ajutorul tău.

Câteva exemple:
    - []        este bine
    - []()      este bine
    - [()()]    este bine
    - ][        nu este bine
    - (][][)    nu este bine
    - [)]()[(]  nu este bine
"""


def get_end_paranteza(paranteza):
    """ Returneaza opusul unei paranteze deschide  """
    if paranteza == '(':
        return ')'
    elif paranteza == '[':
        return ']'
    elif paranteza == '{':
        return '}'


def este_corect(expresie):
    """Verifică dacă toate parantezele sunt folosite corespunzător."""
    stiva = []
    while len(expresie) > 0:
        element = expresie[0]
        expresie = expresie[1:]

        if element in "([{":
            stiva.append(element)

        if element in ")]}":
            if len(stiva) <= 0:
                return False

            if get_end_paranteza(stiva[len(stiva)-1]) != element:
                return False

            stiva.pop()

    return True

if __name__ == "__main__":
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
