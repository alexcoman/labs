#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tuxy

Exemplu de istoric.tuxy:

    STÂNGA 2
    JOS 2
    DREAPTA 5

Fișierul de mai sus ne spune că utilizatorul a mutat cursorul
2 căsuțe la stânga după care 2 căsuțe in jos iar ultima acțiune
a fost să poziționeze cursorul cu 5 căsuțe în dreapta față de
ultima poziție.

El dorește un utilitar care să îi spună care este distanța dintre
punctul de origine (0, 0) și poziția curentă a cursorului.
"""
from __future__ import print_function

import math

DIRECTII = ["STANGA", "DREAPTA", "SUS", "JOS"]


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    try:
        fisier = open("istoric.tuxy", "r")
        comanda = fisier.read()
        fisier.close()
    except IOError:
        print ("Nu am putut obține mesajele.")
        return
    coordonata_x = 0
    coordonata_y = 0
    for i in comanda.splitlines():
        lista_cuvinte = i.split()
        if lista_cuvinte[0] not in DIRECTII:
            print ("Fisierul nu este corect")
            return 0
        if lista_cuvinte[1].isdigit():
            numar = ord(lista_cuvinte[1])
            if lista_cuvinte[0] == 'STANGA':
                coordonata_x -= numar
            elif lista_cuvinte[0] == 'DREAPTA':
                coordonata_x += numar
            elif lista_cuvinte[0] == 'SUS':
                coordonata_y += numar
            elif lista_cuvinte[0] == 'JOS':
                coordonata_y -= numar
        else:
            print ("Fisierul nu este corect")
            return 0
    dist = math.sqrt(coordonata_x**2+coordonata_y**2)
    return dist

if __name__ == "__main__":
    distanta()
