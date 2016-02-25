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


def verifica_expresia(paranteze):
    """Verifică validitatea expresiei primite.

    Verifică dacă toate parantezele din expresie
    sunt folosite corespunzător.
    """
    brackets_stack = []
    for symbol in paranteze:
        if symbol == "[":
            brackets_stack.append(symbol)
        elif symbol == "]":
            if len(brackets_stack) != 0:
                if brackets_stack[len(brackets_stack) - 1] == "[":
                    brackets_stack.pop()
                else:
                    return 0
            else:
                return 0
        elif symbol == "(":
            brackets_stack.append(symbol)
        elif symbol == ")":
            if len(brackets_stack) != 0:
                if brackets_stack[len(brackets_stack) - 1] == "(":
                    brackets_stack.pop()
                else:
                    return 0
            else:
                return 0
    if len(brackets_stack) == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    assert verifica_expresia("[()[]]"), "Probleme la expresia 1"
    assert verifica_expresia("()()[][]"), "Probleme la expresia 2"
    assert verifica_expresia("([([])])"), "Probleme la expresia 3"
    assert not verifica_expresia("[)()()()"), "Probleme la expresia 4"
    assert not verifica_expresia("][[()][]"), "Probleme la expresia 5"
    assert not verifica_expresia("([()]))"), "Probleme la expresia 6"
    assert not verifica_expresia("([)]"), "Probleme la expresia 7"
