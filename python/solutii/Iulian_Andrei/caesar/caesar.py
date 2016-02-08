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


def decripteaza(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 0
    for key in range(26):
        test = ''
        for index in range(3):
            test += alphabet[(alphabet.index(mesaj[index]) + key) % 26]
        if test == 'ave':
            break

    decrypt = ''
    for character in mesaj:
        if character in alphabet:
            decrypt += alphabet[(alphabet.index(character) + key) % 26]
        else:
            decrypt += character

    print decrypt


def main():
    """Functia verifica daca exista erori la deschidere fisierului de
    intrare si, daca nu, apeleaza functia decrripteaza pentru fiecare
    linie din fisier
    """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obține mesajele."
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)

if __name__ == "__main__":
    main()
