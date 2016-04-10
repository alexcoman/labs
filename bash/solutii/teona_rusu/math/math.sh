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


#!/bin/bash
#Autor
#Descriere: 

if [[ $# -ne '2' ]]; then
    echo "Functia nu are 2 parametri."
    exit 1
fi

if [[ ! -f script.sh ]]; then
    echo "Fisierul cu functii nu exista"
    exit 1
else
    . script.sh
fi

meniu()
{
    echo "Meniu:"
    echo -e '\t' 1:Adunare
    echo -e '\t' 2:Scadere
    echo -e '\t' 3:Inmultire
    echo -e '\t' 4:Impartire
    echo -e '\t' 5:Modulo
    echo -e '\t' 0:Exit

    read -p 'Option: ' opt

    case "$opt" in
0)
    exit 0;
    ;;
1)
    n="$(add "$1" "$2")"
    echo "$n"
    ;;
2)
    n="$(substract "$1" "$2")"
    echo "$n"
    ;;
3)
    n="$(multiply "$1" "$2")"
    echo "$n"
    ;;
4)
    if [[ "$2" -eq '0' ]]; then
        echo "Al doilea parametru este 0. Gresit."
        exit 1;
    else
        n="$(divide "$1" "$2")"
        echo "$n"
    fi
    ;;
5)
    n="$(modulo "$1" "$2")"
    echo "$n"
    ;;
*)
    echo "Optiune invalida"
    exit 1;
    ;;

    esac
}

meniu "$1" "$2"

