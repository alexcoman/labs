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
import math


def distanta():
    """Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """

    try:
        in_file = open("istoric.tuxy", "r")
        content = in_file.read()
        in_file.close()
    except IOError:
        print "Error reading file."
        return

    location = [0, 0]
    directions = {"SUS": 1, "JOS": -1, "DREAPTA": 1, "STANGA": -1}

    for line in content.splitlines():
        lista = (line.split())
        nbr = int(lista[1])
        if lista[0] == "SUS" or lista[0] == "JOS":
            for _ in range(nbr):
                location[1] += directions.get(lista[0])
        elif lista[0] == "STANGA" or lista[0] == "DREAPTA":
            for _ in range(nbr):
                location[0] += directions.get(lista[0])
        else:
            print "Error in history."
            return
    return math.sqrt(location[0]**2 + location[1]**2)

if __name__ == "__main__":
    print distanta()
