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


def decripteaza(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    mesaj = mesaj.upper()
    offset = -1
    for deplasament in range(27):
        for cuvant in mesaj.split():
            nume = ""
            for litera in cuvant:
                if litera.isalpha():
                    numar = ord(litera)
                    numar -= ord('A')
                    numar += deplasament
                    numar %= 26
                    numar += ord('A')
                    nume += chr(numar)
            if nume == "CAESAR":
                offset = deplasament
                break
        if offset == deplasament:
            break
    text = ""
    for litera in mesaj:
        if litera.isalpha():
            numar = ord(litera)
            numar -= ord('A')
            numar += offset
            numar %= 26
            numar += ord('A')
            text += chr(numar)
        else:
            text += litera
    print text


def main():
    """dectripteaza mesajul continut in fisierul mesaje.secret"""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obține mesajele."
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)

if __name__ == "__main__":
    main()
