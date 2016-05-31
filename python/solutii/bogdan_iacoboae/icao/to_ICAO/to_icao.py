# *-* coding: UTF-8 *-*
"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.
Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă
Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.
Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    """ Functia pentru ICAO   """
    fisier = open('../../../../date_iesire/mesaj.icao', 'w')
    mesaj = mesaj.lower()
    for cuvant in mesaj.split():
        for litera in cuvant:
            word = ICAO[litera]
            fisier.write(word,)
            fisier.write(" ")
        fisier.write("\n")
    fisier.close()


if __name__ == "__main__":
    icao("Long live python")
