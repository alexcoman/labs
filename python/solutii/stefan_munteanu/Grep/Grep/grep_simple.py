#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy cauta in fiecare zi cate o problema de matematica complet noua pentru el.

Rezolvand problema 101, a observat ca are nevoie de cateva formule mai vechi.
A revenit la fisierierul lui de teoreme "teoreme1.txt" pentru ajutor.
S-a bucurat ca a reusit sa il gaseasca la timp ,fisierierul
fiind in /tmp/ciorne. Uitandu-se prin el,a observat
ca folosea o regula cand scria teoreme noi:

    [Index].[Spatiu][Spatiu][Numele Teoremei]
    [Numele scurt]
    [Rand nou]
    [Rand nou]
    [Teorema]
    [Rand nou]
    [Rand nou]

Exemplu:
    1.  The Irrationality of the Square Root of 2
        SQRT_2_IRRATIONAL
     |- ~rational(sqrt(&2))

Stiind limbajul de programare python si fiind un fan al liniei de comanda,
el doreste sa implementeze un utilitar inteligent de cautat formule.
Functionalitatile care doreste sa le implementeze sunt:
    [1] cautare indiferent de caz (ex. 'a'=='A' ) [-i]

    [2] cautare exacta ( nu ia in considere parti ale cuvintelor) [-e]

    [3] cautare si inlocuire a sirurilor de caractere [-s]


    Ex: python utilitar.py -s "CARD" "CARDINAL"
    fiecare sir "CARD" a fost inlocuit cu "CARDINAL"


    [4] numararea aparitiilor unui sir de caractere [-n]
    [5] cautare recursiva a fisierierelor prin director [-r]
    [6] introducerea parametrilor din linia de comanda:
    ex: python utilitar.py -in "CARD" teoreme1.txt
    sirul "CARD" (insensitiv) apare de 44 de ori in teoreme1.txt
    [7] afisierarea unui mesaj de ajutor daca parametrii introdusi sunt gresiti

P.S. Prin inteligent se refera ca v-a returna tot ce stie despre teorema(nume,
nume scurt siteorema). Daca sirul de caractere cautat apare in mai multe
teoreme, utilitarul returneaza doar numele complet si cel scurt al teoremelor.

Oare cum a implementat Tuxy acest utilitar?

Posibila documentatie:
    - http://linux.die.net/man/1/grep
    - http://git.savannah.gnu.org/cgit/grep.git/snapshot/grep-2.22.tar.gz
    - din cadrul arhivei amintite anterior, folderul "src"
    - https://github.com/heyhuyen/python-grep
"""
from __future__ import print_function

import re
import os


def cautare_indiferenta(mes):
    """ Functie pentru cautarea indiferenta """
    fisier = open("teoreme1.txt", "r")
    if numar_aparitii(mes) == 1:
        verif = 0
        numar = 0
        for linie in fisier:
            linie = linie.rstrip()
            if mes.lower() in linie.lower():
                verif = 1
                numar = 0
            r_obj = re.search(r'\d+\\.  ', linie)
            if r_obj:
                numar += 1
            if numar == 2:
                verif = 0
            if numar < 2 and verif:
                print(linie)
    else:
        verif = 0
        numar = 0
        for linie in fisier:
            linie = linie.rstrip()
            if mes.lower() in linie.lower():
                verif = 1
                numar = 0
            numar += 1
            if numar == 3:
                verif = 0
            if numar < 3 and verif:
                print(linie)


def cautare_exacta(mes):
    """ Functie pentru cautarea exacta """
    fisier = open("teoreme1.txt", "r")
    mes = " " + mes + " "
    if numar_aparitii(mes) == 1:
        verif = 0
        numar = 0
        for linie in fisier:
            linie = linie.rstrip()
            if mes in linie:
                verif = 1
                numar = 0
            r_obj = re.search(r'\d+\\.  ', linie)
            if r_obj:
                numar += 1
            if numar == 2:
                verif = 0
            if numar < 2 and verif:
                print(linie)
    else:
        verif = 0
        numar = 0
        for linie in fisier:
            linie = linie.rstrip()
            if mes in linie:
                verif = 1
                numar = 0
            numar += 1
            if numar == 3:
                verif = 0
            if numar < 3 and verif:
                print(linie)


def cautare_inlocuire_print(mes, inl):
    """ Functie pentru cautarea si inlocuirea mesajului """
    fisier = open("teoreme1.txt", "r")
    for linie in fisier:
        if mes in linie:
            print(linie.replace(mes, inl))


def numar_aparitii(mes):
    """ Functie pentru numarul de aparitii """
    fisier = open("teoreme1.txt", "r")
    lista = [item for item in fisier]
    point = str(lista).count(mes)
    return point


def parcurgere_dupa_nume_fisier(*args):
    """Apeleaza recursiv executia grep pe fisierele din director."""
    argument = args[len(args) - 1]
    if os.path.isdir(os.path.abspath(argument)):
        for fisier in os.listdir(argument):
            if os.path.isdir(os.path.join(argument, fisier)):
                parcurgere_dupa_nume_fisier(
                    list(args[:len(
                        args) - 1]) + [os.path.join(argument, fisier)])
        print ("There is a folder by that name.")
    else:
        print ("Not a folder!")


if __name__ == "__main__":
    OPERATION = raw_input('->').split(' ')
    if OPERATION[0] == "-i" and len(OPERATION) == 2:
        print("Cautare indiferenta")
        cautare_indiferenta(OPERATION[1])
    elif OPERATION[0] == "-e" and len(OPERATION) == 2:
        print("Cautare exacta:")
        cautare_exacta(OPERATION[1])
    elif OPERATION[0] == "-s" and len(OPERATION) == 3:
        print("Inlocuire in afisare:")
        cautare_inlocuire_print(OPERATION[1], OPERATION[2])
    elif OPERATION[0] == "-n" and len(OPERATION) == 2:
        print("Numar aparitii:")
        print(numar_aparitii(OPERATION[1]))
    elif OPERATION[0] == "-r" and len(OPERATION) == 3:
        print("Cautare folder:")
        parcurgere_dupa_nume_fisier(OPERATION[1], OPERATION[2])
    elif OPERATION[0] == "-help" and len(OPERATION) == 1:
        print("Cautare indiferenta: -i <word>")
        print("Cautare exacta: -e <word>")
        print("Inlocire: -s <word> <word_replace>")
        print("Numar aparitii: -n <word>")
        print("Cautare folder: -r <word>")
    else:
        print("Parametri sunt afisati gresit, incearca -help")
