#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy cauta in fiecare zi cate o problema de matematica complet noua pentru el.

Rezolvand problema 101, a observat ca are nevoie de cateva formule mai vechi.
A revenit la fisierul lui de teoreme "teoreme1.txt" pentru ajutor. S-a bucurat
ca a reusit sa il gaseasca la timp ,fisierul fiind in /tmp/ciorne.
Uitandu-se prin el,a observat ca folosea o regula cand scria teoreme noi:

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
    [5] cautare recursiva a fisierelor prin director [-r]
    [6] introducerea parametrilor din linia de comanda:
    ex: python utilitar.py -in "CARD" teoreme1.txt
    sirul "CARD" (insensitiv) apare de 44 de ori in teoreme1.txt
    [7] afisarea unui mesaj de ajutor daca parametrii introdusi sunt gresiti

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
import argparse
import os
import copy
import re


def afisare_basic(teorema, args):
    """ afisare basic a informatiilor unei teoreme """
    if not args.count:
        print(teorema["nume"].strip())
        print(teorema["numeScurt"].strip())


def afisare(teorema, args):
    """ afishare scurta a unei teoreme """
    if not args.count:
        afisare_basic(teorema, args)
        print()


def afisare_complet(teorema, args):
    """ afishare completa a unei teoreme """
    if not args.count:
        afisare_basic(teorema, args)
        print(teorema['teorema'].strip())
        print()


def is_valid(teorema, args):
    """ verifica daca o teorema respecta conditiile """
    if args.ignore_case:
        for value in teorema.values():
            if args.pattern.lower() in value.lower():
                return True
    else:
        for value in teorema.values():
            if args.pattern in value:
                return True

    return False


def parse_file_from_directory(path, args):
    """ parseaza toate fisierele din path/* """
    try:
        fisier = open(path, 'r')
    except IOError:
        print("Nu am putut deschide fisierul :", path)
        return
    first_teorema = {}
    teorema = {
        "nume": "",
        "numeScurt": "",
        "teorema": ""
        }
    n_spaces = 0
    n_found = 0

    for line in fisier:
        if line.strip() == "":
            n_spaces += 1

        if "." in line:
            index = line[:line.find(".")]
            try:
                index = int(index)
                teorema["nume"] = line
                teorema["teorema"] = ""
                n_spaces = 0
            except ValueError:
                pass

        if n_spaces == 0:
            teorema["numeScurt"] = line
        elif n_spaces == 2:
            teorema["teorema"] += line
        elif n_spaces == 4 and is_valid(teorema, args):
            n_found += 1
            if n_found == 1:
                first_teorema = copy.copy(teorema)
            elif n_found == 2:
                afisare(first_teorema, args)
                afisare(teorema, args)
            elif n_found > 2:
                afisare(teorema, args)

    fisier.close()
    if n_found == 1:
        afisare_complet(first_teorema, args)


def parse_dir(args, dirname, names):
    """ parseaza un director, primeste argumentele comenzi, numele directorului
    si pathurile din director
    """
    for name in names:
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            parse_file_from_directory(path, args)


def parse_file_count(path, args):
    """ count number of aparitions of pattern dintr-un fisier """
    try:
        fisier = open(path, 'r')
    except IOError:
        print("Nu am putut deschide fisierul :", path)
        return
    n_found = 0
    pattern = args.pattern
    for line in fisier:
        if args.ignore_case:
            line = line.lower()
            pattern = pattern.lower()
        n_found += line.count(pattern)

    fisier.close()
    return n_found


def parse_file_replace(path, args):
    """ inlocuieste aparitia unui pattern intr-un fisier """
    try:
        fisier = open(path, 'r')
    except IOError:
        print("Nu am putut deschide fisierul :", path)
        return
    full_data = fisier.read()
    fisier.close()

    try:
        fisier = open(path, "w+")
    except IOError:
        print("Nu am putut deschide fisierul :", path)
        return

    data = ""
    for line in full_data:
        data += line

    if args.ignore_case:
        pattern = re.compile(re.escape(args.pattern), re.IGNORECASE)
        pattern.sub(args.pattern, data)
    else:
        data = data.replace(args.pattern, args.replace)

    fisier.write(data)
    fisier.close()


def parse_dir_replace(args, dirname, names):
    """ inlocuieste un pattern intr-un director """
    for name in names:
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            parse_file_replace(path, args)


def parser_arguments():
    """ parseaza argumentele primite la rularea programului """
    args = argparse.ArgumentParser()
    args.add_argument('path',
                      type=str, help="unde cautam")
    args.add_argument('pattern',
                      type=str, help="tiparul de gasit")
    args.add_argument("-i", "--ignore_case",
                      help="Ignore case", action="store_true")
    args.add_argument("-e", "--exact",
                      help="cautare exacta\
                              (nu ia in considerare parti ale cuvintelor)",
                      action="store_true")
    args.add_argument("-r", "--recursive",
                      help="cautare recursiva in fisier dat ca <pattern> ",
                      action="store_true")
    args.add_argument("-n", "--count",
                      help="numara de cate ori gasim patternul",
                      action="store_true")
    args.add_argument("-s", "--replace",
                      help="inlocuieste <patternul> cu <string>")

    args = args.parse_args()
    return args


def count(args):
    """ count aparition of a pattern """
    path = os.path.abspath(args.path)
    total = 0

    if args.recursive:
        if os.path.exists(args.path):
            for item in os.listdir(path):
                little_path = os.path.join(path, item)
                if os.path.isfile(little_path):
                    total += parse_file_count(little_path, args)
                else:
                    total += count(little_path)
        else:
            print("EROARE: <" + args.path +
                  "> invalid, nu putem ajunge acolo")
    else:
        if os.path.isfile(args.path):
            total += parse_file_count(args.path, args)
        else:
            print("EROARE: <" + args.pattern +
                  "> invalid, nu este fisier")
    return total


def replace(args):
    """ replace a pattern """
    if args.recursive:
        if os.path.exists(args.path):
            os.path.walk(args.path, parse_dir_replace, args)
        else:
            print("EROARE: <" + args.path +
                  "> invalid, nu putem ajunge acolo")
    else:
        if os.path.isfile(args.path):
            parse_file_replace(args.path, args)
        else:
            print("EROARE: <" + args.pattern +
                  "> invalid, nu este fisier")
    return


def main():
    """ main """
    args = parser_arguments()

    if args.count:
        print("Am gasit: ", count(args))

    if args.replace:
        replace(args)
    if args.recursive:
        if os.path.exists(args.path):
            os.path.walk(args.path, parse_dir, args)
        else:
            print("EROARE: <" + args.path + "> invalid, nu putem ajunge acolo")
    else:
        path = os.path.abspath(args.path)
        if os.path.isfile(path):
            parse_file_from_directory(path, args)
        else:
            print("EROARE: <" + args.pattern + "> invalid, nu este fisier")


if __name__ == "__main__":
    main()
