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
# pylint: disable=unused-argument

from __future__ import print_function


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    list_chars_of_message = list(mesaj)

    key = ord(list_chars_of_message[0]) - ord('a')

    returned_list = []

    for i in list_chars_of_message:

        if ord(i) < 97 or ord(i) > 122:
            returned_list.append(i)
        else:

            if ord(i) - key >= 97 and ord(i) - key <= 122:
                returned_list.append(chr(ord(i) - key))

            elif ord(i) - key < 97:

                until_last_letter = ord(i) - ord('a')

                decrypted_letter = chr(ord('z') - key + until_last_letter + 1)

                returned_list.append(decrypted_letter)

    returned_message = ''.join(returned_list)

    print(returned_message)


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
