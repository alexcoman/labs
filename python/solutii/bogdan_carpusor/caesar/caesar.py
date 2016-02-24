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


def generate_message(character, key, dictionary):
    index = dictionary.find(character)
    if index > 0:
        return dictionary[index + key]
    else:
        return character


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    key = 0
    dictionary = "abcdefghijklmnopqrstuvwxyz"
    key_phrase = "ave caesar"
    for displacement in range(1, 13):
        message_head = list(mesaj[0:len(key_phrase)])
        for character in message_head:
            if dictionary.find(character) > 0:
                if chr(ord(character) + displacement) == \
                        key_phrase[message_head.index(character)]:
                    key = displacement
                elif chr(ord(character)-displacement) == \
                        key_phrase[message_head.index(character)]:
                    key = -displacement

    message_list = [generate_message(character, key, dictionary)
                    for character in mesaj]
    decoded_message = "".join(message_list)
    print ("Deciphred message:")
    print (decoded_message)


def main():
    """ Functia citeste un fisier si aplica metoda de
    decriptare pe textul din cadrul fisierului
    """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)
        print()

if __name__ == "__main__":
    main()
