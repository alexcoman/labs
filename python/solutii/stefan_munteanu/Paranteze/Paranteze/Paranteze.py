"""Tuxy scrie in fiecare zi foarte multe formule matematice.

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


def verifica_expresia(paranteze):
    """Verifica validitatea expresiei primite.

    Verifica daca toate parantezele din expresie
    sunt folosite corespunzator.
    """
    if len(paranteze) % 2 != 0:
        return False
    deschide_paranteze = set('([')
    tipuri_paranteze = ([('(', ')'), ('[', ']')])
    lista = []
    for char in paranteze:
        if char in deschide_paranteze:
            lista.append(char)
        else:
            if len(lista) == 0:
                return False
            ultima_deschisa = lista.pop()
            if (ultima_deschisa, char) not in tipuri_paranteze:
                return False
    return len(lista) == 0


if __name__ == "__main__":
    assert verifica_expresia("[()[]]"), "Probleme la expresia 1"
    assert verifica_expresia("()()[][]"), "Probleme la expresia 2"
    assert verifica_expresia("([([])])"), "Probleme la expresia 3"
    assert not verifica_expresia("[)()()()"), "Probleme la expresia 4"
    assert not verifica_expresia("][[()][]"), "Probleme la expresia 5"
    assert not verifica_expresia("([()]))"), "Probleme la expresia 6"
    assert not verifica_expresia("([)]"), "Probleme la expresia 7"
