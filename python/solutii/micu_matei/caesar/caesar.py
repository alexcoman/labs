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


def get_letter(caracter, cifru):
    """ decripteaza un caracter folosind cifrul """
    if caracter.isalpha():
        caracter = ord(caracter) - cifru
        if caracter < ord('a'):
            caracter = ord('z') - abs(ord('a')-caracter) + 1
        return chr(caracter)
    else:
        return caracter


def get_line(linie, cifru):
    """ decripteaza o linie folosind cifrul """
    return "".join([get_letter(caracter, cifru) for caracter in linie])


def decripteaza(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    first_letter = 'a'
    key = 0
    for posibil_cifru in range(25):
        if get_letter(mesaj[0], posibil_cifru).lower() == first_letter:
            key = posibil_cifru
            break

    print(get_line(mesaj, key))


def main():
    """ functia main """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele..")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)


if __name__ == "__main__":
    main()
