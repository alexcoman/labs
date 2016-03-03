#!/bin/bash

# Sa se scrie un script care implementeaza operatiile matematice de baza ( +, -, *,
# /, %). Scriptul va primi ca parametri doar operanzii. Scriptul afiseaza un meniu
# de unde se poate selecta una din operatiile disponibile. Daca utilizatorul
# selecteaza alta optiune, scriptul isi va incheia executia afisand un mesaj de
# terminare. Operatiile vor fi implementate prin functii scrise intr-un fisier separat.
# Scriptul va testa existenta fisierului de functii iar daca acesta exista il va incarca,
# altfel va afisa un mesaj de eroare. Pentru meniu trebuie scrisa o functie.
# Restrictii:
# - functia pentru afisarea meniului nu se scrie in fisierul ce contine functiile
# pentru operatii.
# - pentru implementarea meniului se va folosi o structura de control de tip
# case.
# - maxim 2 fisiere (scriptul principal si fisierul de functii matematice)

if [ -e ./functions_math.src ]; then
    source ./functions_math.src
else
    echo "Nu am putut deschide fisierul de functii"
    exit
fi


echo "Apasati tasta corespunzatoare operatieo "
echo "1 = +"
echo "2 = -"
echo "3 = *"
echo "4 = /"
echo "5 = %"

read select

case "$select" in
    1)
        add "$1" "$2"
        ;;
    2)
        sub "$1" "$2"
        ;;
    3)
        mult "$1" "$2"
        ;;
    4)
        div "$1" "$2"
        ;;
    5)
        mod "$1" "$2"
        ;;
    *)
        printf "Utilizare: %s {1|2|3|4|5}" "$0"
esac
