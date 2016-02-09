"""
Transform given input file from ICAO standard to normal text
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


def din_icao(fisier_intrare, fisier_iesire):
    """
    va genera un fisier numit icao_intrare
    ce va contine mesajul initial.
    :param fisier_intrare: File containing a message encrypted with ICAO
    :param fisier_iesire: The file containing the decrypted message
    :return: A file containing the decrypted message
    """
    words = [x for x in fisier_intrare.split()]
    for i in words:
        fisier_iesire.write(i[0])
    fisier_iesire.write(' ')


def main():
    """
    The main function
    :return: returns the message
    """
    try:
        fisier = open("mesaj.icao", "r")
        mesaj_icao = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obtine mesajele.")
        return
    output = open('./mesajul.txt', 'w+')
    for mesaj in mesaj_icao.splitlines():
        if mesaj.strip():
            din_icao(mesaj, output)

if __name__ == "__main__":
    main()
