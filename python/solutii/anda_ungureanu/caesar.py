#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.
Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj si tu ai fost ales să descifrezi
misterul.
Informatii:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe pozitia aflată
la un n pasi de ea în alfabet (unde este n este un număr întreg cunoscut
"""
from __future__ import print_function


def decripteaza(mesaj):
    """
    Functi primeste ca parametru o linie de mesaj ce trebuie decriptat
    si un numar. Fiecare litera este inlocuita cu cea de la numarul
    intorduse pasi in urma. Cand se gaseste cuvantul "ave" randul este
    considerat valid si mesajul este afisat, altfel este incrementat
    numarul de pasi.
    """
    nr_pasi = 0
    mess = ['']
    mess_final = " "
    while "ave" not in mess_final:
        for litera in mesaj:
            if litera.isalpha():
                if (ord(litera) - nr_pasi >= 97 and
                        ord(litera) - nr_pasi <= 122):
                    litera_m = chr(ord(litera)-nr_pasi)
                else:
                    litera_m = chr(122-(nr_pasi-(ord(litera)-97)-1))
                mess.append(litera_m)
            else:
                mess.append(litera)
        mess_final = "".join(mess)
        if 'ave' not in mess_final:
            mess = ['']
            mess_final = " "
            nr_pasi = nr_pasi+1
    print(mess_final)


def main():
    """
    Se incearca deschiderea fisierului de intrare, daca operatia este
    executata cu succes, se apeleaza functia de decriptare.
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
