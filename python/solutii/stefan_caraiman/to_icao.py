"""Transform the given message to the ICAO standard"""

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    """
    :param mesaj: The message to generate to ICAO
    :return: A file containing the encrypted message
    """
    for i in mesaj.lower():
        if i.isalpha():
            OUTPUT.write(ICAO[i] + ' ')
        elif i.isspace():
            OUTPUT.write(' ')


if __name__ == "__main__":
    OUTPUT = open('./mesaj.icao_intrare', 'w+')
    icao("Mesajul ce trebuie transmis")
