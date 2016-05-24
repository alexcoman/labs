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
# pylint: disable=unused-argument


def paranteza_deschisa(paranteza):
    if paranteza == ')':
        return '('
    elif paranteza == ']':
        return '['
    else:
        return ''


def verifica_expresia(paranteze):
    """Verifică validitatea expresiei primite.

    Verifică dacă toate parantezele din expresie
    sunt folosite corespunzător.
    """

    paranteze_stiva = [];

    for idx in range(0, len(paranteze) - 1):

        if paranteze[idx] == '(' or paranteze[idx] == '[':
            paranteze_stiva.append(paranteze[idx])
        elif paranteze[idx] == ')' or paranteze[idx] == ']':
            if not paranteze_stiva or paranteze_stiva.pop() != paranteza_deschisa(paranteze[idx]):
                return False

    return paranteze_stiva


if __name__ == "__main__":
    assert verifica_expresia("[()[]]"), "Probleme la expresia 1"
    assert verifica_expresia("()()[][]"), "Probleme la expresia 2"
    assert verifica_expresia("([([])])"), "Probleme la expresia 3"
    assert not verifica_expresia("[)()()()"), "Probleme la expresia 4"
    assert not verifica_expresia("][[()][]"), "Probleme la expresia 5"
    assert not verifica_expresia("([()]))"), "Probleme la expresia 6"
    assert not verifica_expresia("([)]"), "Probleme la expresia 7"
