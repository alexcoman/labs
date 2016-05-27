#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Problema caesar"""

from __future__ import print_function


def decripteaza_mesajul(mesaj):
    """Decriptare mesaj."""
    cheie = ord(mesaj[0]) - ord('a')
    mesaj_dec = []
    for car in mesaj:
        if car.isalpha():
            index = ord(car)-cheie
            if index < ord('a'):
                mesaj_dec.append(chr(ord('z')-ord('a')+index+1))
            else:
                mesaj_dec.append(chr(index))
        else:
            mesaj_dec.append(car)
    print("".join(mesaj_dec))


def main():
    """functia main"""
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
