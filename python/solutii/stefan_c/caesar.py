"""Module implementing the caesar cipher"""
# !/usr/bin/env python
# *-* coding: UTF-8 *-*
from __future__ import print_function


def cipher(word):
    """
    :param word: the word to decipher to "ave"
    :return: the number used for encryption
    """
    word = word.lower()
    return ord(word[0]) % 97


def decripteaza(mesaj):
    """
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
        if (not chr(char).isalpha() and chr(char) != ' ') or (chr(char).isupper()):
            char += 26
        mesaj_decriptat += chr(char)
    print (mesaj_decriptat)


def main():
    """
    The main function
    :return: all the decrypted messages
    """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obtine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)


if __name__ == "__main__":
    main()
