#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuviânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.

Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""
from __future__ import print_function

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def read_file(file_path):
    """Functia primeste citeste un fisier
    si returneaza continutul fisierului respectv
    """
    try:
        input_file = open(file_path)
        message = input_file.read()
        input_file.close()
    except IOError:
        print ("Could not open file")
        return

    return message


def din_icao(mesaj):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """
    message = read_file(mesaj)
    words_list = []
    word_lines = message.splitlines()
    inverted_dictionary = {value: key for key, value in ICAO.items()}
    word_lines.pop()
    for line in word_lines:
        words = line.split(" ")
        temp_list = [inverted_dictionary[word]
                     for word in words]

        words_list.append("".join(temp_list))
        words_list.append(" ")
    decoded_message = "".join(words_list)

    file_output = open("icao.intrare", "w+")
    file_output.write(decoded_message)
    file_output.close()

if __name__ == "__main__":
    din_icao("../../../date_intrare/mesaj.icao")
