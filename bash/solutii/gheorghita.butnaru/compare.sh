#!/bin/bash

# Sa se scrie un fisier de comenzi, care verifica daca doua directoare sunt egale.
# Numele celor doua directoare se transmit ca argumente in linia de comanda. Doua
# directoare se considera ca sunt egale daca contin aceleasi subdirectoare si fisiere.
# Se utilizeaza comanda diff.


if ! [ -d "$1" ] || ! [ -d "$2" ];then
    printf "Usage: %s dir1 dir2\n" "$0"
    printf "Directoarele date trebuie sa existe\n"
    exit
fi
cmp=$(diff -r "$1" "$2")
if [ "$cmp" == "" ]; then
    echo "Sunt egale!"
else
    echo "Nu sunt egale!"
fi

