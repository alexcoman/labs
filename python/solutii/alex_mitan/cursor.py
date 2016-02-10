#!/usr/bin/env py_crdthon
# *-* coding: UTF-8 *-*

"""Tux_crdy_crd dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tux_crdy_crd

Ex_crdemplu de istoric.tux_crdy_crd:

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


def distanta():
    """Calculates the distance between two (X,Y) points from a file"""
    x_crd = 0
    y_crd = 0
    raw = open("istoric.tuxy").read().splitlines()
    direction = ""
    amount = 0
    for item in raw:

        direction = item.split()[0]
        amount = int(item.split()[1])

        if direction == "SUS":
            x_crd += amount
        elif direction == "JOS":
            x_crd -= amount
        elif direction == "STANGA":
            y_crd -= amount
        elif direction == "DREAPTA":
            y_crd += amount
        else:
            print "Error, history_crd invalid"

    print "Final x_crd = " + str(x_crd)
    print "Final y_crd = " + str(y_crd)

    distance = (x_crd * x_crd + y_crd * y_crd) ** 0.5
    print "Distanta: " + str(distance)


if __name__ == "__main__":
    distanta()
