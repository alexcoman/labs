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


def distanta(istoric):
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    istoric = istoric.read()
    position = [0, 0]
    for lines in istoric.splitlines():
        line = lines.split()
        if line[0] == ('STANGA'):
            position[0] += -int(line[1])
        elif line[0] == ('DREAPTA'):
            position[0] += +int(line[1])
        elif line[0] == ('SUS'):
            position[1] += +int(line[1])
        elif line[0] == ('JOS'):
            position[1] += -int(line[1])
    print((position[0] ** 2 + position[1] ** 2) ** 0.5)


def main():
    """
    Se incearca deschiderea fisierului. In caz de succes acesta este
    transmis functiei distanta()
    """
    try:
        istoric = open("../../../date_intrare/istoric.tuxy", "r")
    except IOError:
        print("Nu am putut citi fisierul")
        return
    distanta(istoric)


if __name__ == "__main__":
    main()
