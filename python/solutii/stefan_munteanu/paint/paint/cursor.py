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
punctul de origine (0, 0) și poziția curentă a cursorului."""
import math


DIRECTII_VALIDE = ["SUS", "JOS", "STANGA", "DREAPTA"]


def validare_inscructiune(instructiue):
    """Testeaza pentru validitatea mutarii"""
    if instructiue in DIRECTII_VALIDE:
        return True
    return False


def calc(directie, valoare):
    """Adauga"""
    pozitie_pcty = 0
    pozitie_pctx = 0
    if directie == "SUS":
        pozitie_pcty += valoare
    if directie == "JOS":
        pozitie_pcty -= valoare
    if directie == "STANGA":
        pozitie_pctx -= valoare
    if directie == "DREAPTA":
        pozitie_pctx += valoare
    return float(pozitie_pctx), float(pozitie_pcty)


def distanta():
    """Calculează distanța dintre origine și poziția curentă.
    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului."""
    istoric = open("istoric.tuxy", "r")
    instructiunii = istoric.read()
    instructiunii = instructiunii.splitlines()
    istoric.close()
    for instructiune in instructiunii:
        comenzi = instructiune.split(' ')
        if validare_inscructiune(comenzi[0]):
            pozitie_pctx, pozitie_pcty = calc(comenzi[0], int(comenzi[1]))
        else:
            return 0
    print math.sqrt(pow(0 - pozitie_pctx, 2) + pow(0 - pozitie_pcty, 2))

if __name__ == "__main__":
    distanta()