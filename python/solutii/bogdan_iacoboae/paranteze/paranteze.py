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
    """ Functia care verifica parantezele """
    lista = []
    for index in paranteze:
        if index == '(' or index == '[':
            lista.append(index)
        elif len(lista) > 0:
            if index == ')' and lista[-1] == '(':
                lista.pop()
            elif index == ']' and lista[-1] == '[':
                lista.pop()
            else:
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    if verifica_expresia(raw_input("Give me your parenthesis : ")):
        print "Parantezele au fost puse bine"
    else:
        print "Parantezele nu au fost puse bine"
