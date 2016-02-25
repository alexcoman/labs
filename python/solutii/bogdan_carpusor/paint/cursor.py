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
from copy import deepcopy


def read_file(file_path):
    """Functia citeste continutul fisierului
    si returneaza continutul acestuia
    """
    try:
        input_file = open(file_path)
        text_content = input_file.read()
        input_file.close()
        return text_content
    except IOError:
        print ("Can not read from file")


def parse_file(line, position):
    """Functia preia comenzi din fisier
    si stabileste noua pozitie
    """
    movement = line.split(" ")
    if movement[0] == "SUS":
        position["x"] += float(movement[1])
    elif movement[0] == "JOS":
        position["x"] -= float(movement[1])
    elif movement[0] == "STANGA":
        position["y"] -= float(movement[1])
    elif movement[0] == "DREAPTA":
        position["y"] += float(movement[1])
    else:
        print("Incorrect input")


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    origin = {"x": 0.0, "y": 0.0}
    current_position = deepcopy(origin)

    try:
        text_content = read_file("../../../date_intrare/istoric.tuxy")
    except Exception as error:
        print (repr(error))
        return

    for file_line in text_content.splitlines():
        parse_file(file_line, current_position)

    print ("Final position: %d %d" %
           (current_position["x"], current_position["y"]))
    print ("Starting position: %d %d" % (origin["x"], origin["y"]))
    distance = ((origin["x"] - current_position["x"])**2 +
                (origin["y"] - current_position["y"])**2) ** 0.5
    print ("Distance between points: %d" % distance)

if __name__ == "__main__":
    distanta()
