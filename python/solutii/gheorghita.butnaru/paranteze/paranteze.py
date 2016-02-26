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


from __future__ import print_function


def verifica_expresia(paranteze):
    """Verifică validitatea expresiei primite.

    Verifică dacă toate parantezele din expresie
    sunt folosite corespunzător.
    """
    if not paranteze:
        print("Nu am primit expresie de evaluat")
    else:
        parant = {'opening': '{[(', 'closing': '}])'}
        stack = []
        for symbol in paranteze:
            if symbol in parant['opening']:
                stack.append(symbol)
            elif symbol in parant['closing']:
                if len(stack) == 0:
                    return False
                else:
                    index_parant_cl = parant['closing'].index(symbol)
                    parant_test = parant['opening'][index_parant_cl]
                    if stack.pop() != parant_test:
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
