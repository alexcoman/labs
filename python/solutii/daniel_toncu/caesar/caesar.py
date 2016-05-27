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
import os


def decrypt_letter(letter, key):

    """
    Functia, decripteaza, conform Cifrului lui Caesar,
    litera letter cu cheia key.
    """

    if letter.isalpha():
        letter_ord = ord(letter) - key
        if letter_ord < ord('a'):
            letter_ord = ord('z') - (ord('a') - letter_ord - 1)
        return chr(letter_ord)

    return letter


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """

    key = ord(mesaj[0]) - ord('a')

    return "".join(decrypt_letter(letter, key) for letter in mesaj)


def main():
    """ Main function docstring """
    try:
        fisier = open(os.path.join("..", "..", "..", "date_intrare",
                                   "mesaje.secret"), "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()
