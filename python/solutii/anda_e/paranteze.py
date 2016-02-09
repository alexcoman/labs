#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy scrie in fiecare zi foarte multe formule matematice.
Pentru ca formulele sunt din ce in ce mai complicate trebuie
sa foloseasca o serie de paranteze si a descoperit ca cea
mai frecventa problema a lui este ca nu toate parantezele
sunt folosite cum trebuie.
Pentru acest lucru a apelat la ajutorul tau.
Cateva exemple:
    - []        este bine
    - []()      este bine
    - [()()]    este bine
    - ][        nu este bine
    - (][][)    nu este bine
    - [)]()[(]  nu este bine
"""


def este_corect(expresie):
    """Verifica daca toate parantezele sunt folosite corespunzator."""
    vect_paranteze = ['!']
    for paranteza in expresie:
        if paranteza is '(' or paranteza is '[':
            vect_paranteze.append(paranteza)
        if paranteza is ')':
            if vect_paranteze.pop() is '(':
                pass
            else:
                return False
        if paranteza is ']':
            if vect_paranteze.pop() is'[':
                pass
            else:
                return False
    return vect_paranteze.pop() is '!'


if __name__ == "__main__":
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
