"""
Find distance between origin point and another distance
"""
from __future__ import print_function
from math import sqrt


CARDINAL_POINTS = ["SUS", "JOS", "STANGA", "DREAPTA"]


def validinstruction(instruction):
    """
    Check whether the given instruction is valid
    :param instruction: a cardinal point
    :return: If the instruction is a valid input
    """
    if instruction in CARDINAL_POINTS:
        return True
    return False


def distanta():
    """
    Computes the distance between the origin point (0, 0)
     and the current cursor position
    :return: the distance between the two
    """
    try:
        istoric = open("istoric.tuxy", "r")
        instructions = istoric.read()
        instructions = instructions.splitlines()
        positionx, positiony = 0, 0
        istoric.close()
    except IOError:
        print("Could not open file.")
        return
    for instruction in instructions:
        commands = instruction.split(' ')
        if validinstruction(commands[0]):
            if commands[0] == "SUS":
                positiony += int(commands[1])
            if commands[0] == "JOS":
                positiony -= int(commands[1])
            if commands[0] == "STANGA":
                positionx -= int(commands[1])
            if commands[0] == "DREAPTA":
                positionx += int(commands[1])
        else:
            return 0
    return sqrt(pow(0 - positionx, 2) + pow(0 - positiony, 2))


if __name__ == "__main__":
    print(distanta())
