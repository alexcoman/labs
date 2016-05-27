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


def paranteza_deschisa(paranteza):

    """
    Functia returneaza, pentru un tip de paranteza inchisa, acelasi tip
    de paranteza dar deschisa.
    Astfel: ')' => '(', ']' => '['.
    """

    if paranteza == ')':
        return '('
    if paranteza == ']':
        return '['


def verifica_expresia(paranteze):
    """Verifică validitatea expresiei primite.

    Verifică dacă toate parantezele din expresie
    sunt folosite corespunzător.
    """

    stiva_de_paranteze = []

    for idx in range(0, len(paranteze) - 1):
        if paranteze[idx] == '(' or paranteze[idx] == '[':
            stiva_de_paranteze.append(paranteze[idx])
        elif paranteze[idx] == ')' or paranteze[idx] == ']':
            if (not stiva_de_paranteze or
                    (stiva_de_paranteze.pop() !=
                     paranteza_deschisa(paranteze[idx]))):
                return False

    if not stiva_de_paranteze:
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
