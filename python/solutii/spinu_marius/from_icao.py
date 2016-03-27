#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.
Pent-ru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă
Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.
Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""
# pylint: disable=unused-argument

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(mesaj):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """

    try:
        my_file = open(mesaj)
        strings = my_file.read()
        my_file.close()
    except IOError:
        print "Error encountered"
        return

    final_list_of_lines = []

    for line in strings.splitlines():
        processed_list = []

        if line[0] in ICAO:
            processed_list.append(line[0])

        for i, obj in enumerate(line):
            if obj == ' ':
                if line[i + 1] in ICAO and line[i + 1]:
                    processed_list.append(line[i + 1])

        processed_list.append('\n')
        current_row = ''.join(processed_list)

        final_list_of_lines.append(current_row)

    try:
        output_file = open("output.txt", "r+")
        message = ''.join(final_list_of_lines)
        output_file.write(message)
        output_file.close()
    except IOError:
        print "Error encountered"
        return


if __name__ == "__main__":
    din_icao("mesaj.icao")
