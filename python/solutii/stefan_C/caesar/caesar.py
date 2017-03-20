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


def cipher(word):
    """Cipher.

    :param word: the word to decipher to "ave"
    :return: the number used for encryption
    """
    word = word.lower()
    return ord(word[0]) % 97


def decripteaza(mesaj):
    """Decripteaza.

    :param mesaj: Mesajul pe care vrem sa il decriptam
    :return: va return cate un sir de cuvinte decriptat
    """
    words = mesaj.split('.,')
    key = cipher(words[0])
    mesaj_decriptat = ' '
    for i in mesaj.lower():
        char = ord(' ')
        if i.isalpha():
            char = (ord(i)-key)
        if (not chr(char).isalpha() and chr(char) != ' ') or (
                chr(char).isupper()):
            char += 26
        mesaj_decriptat += chr(char)
    print (mesaj_decriptat)


def main():
    """Main."""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)


if __name__ == "__main__":
    main()
