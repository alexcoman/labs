#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""

from __future__ import print_function


def decriptare(sir):
    """Functia cauta cheie pentru decriptare"""
    sir = ord(sir)
    nr_cheie = sir - ord('a')
    return nr_cheie


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    nr_cheie = decriptare(mesaj[0])
    lista = []
    for caracter in mesaj:
        if caracter.isalpha() and caracter.islower():
            if (ord(caracter)-nr_cheie) < ord('a'):
                nr_cheie2 = ord('a') - ord(caracter) + nr_cheie - 1
                lista.append(chr(ord('z')-nr_cheie2))
            else:
                lista.append(chr(ord(caracter)-nr_cheie))
        else:
            lista.append(caracter)
    mesaj_nou = "".join(lista)
    print (mesaj_nou)


def main():
    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()
