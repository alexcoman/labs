#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.

Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""


def din_icao(fisier_intrare):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """
    mesajdecriptat = []
    with open(fisier_intrare, "r") as fin:
        for mesaj in fin:
            strn = mesaj.split()
            for index in strn:
                mesajdecriptat.append(index[0])
            mesajdecriptat.append(' ')
    out = open("icao_intrare", "w")
    out.write("".join(mesajdecriptat))
    out.close()

if __name__ == "__main__":
    din_icao("mesaj.icao")
