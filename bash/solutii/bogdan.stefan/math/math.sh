#!/bin/bash

#Author: Bogdan Stefan
#Description: Fisier de baza pentru exercitiul math

if [[ $# -ne '2' ]]; then
    echo "Fisierul primeste 2 parametri. Exemplu: ./$0 10 20"
    exit 1
fi

if [[ ! -f script.sh ]]; then
    echo "fisier cu functii nu exista"
    exit 1
else
    . script.sh
fi

meniu ()
{
    echo "Meniu:"
    echo -e '\t' 1:Adunare
    echo -e '\t' 2:Scadere
    echo -e '\t' 3:Multiply
    echo -e '\t' 4:Divide
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
        echo "Al doilea parametru este 0. Iesim..."
        exit 1
    else
        n="$(divide "$1" "$2")"
        echo "$n"
    fi
    ;;
5)
    if [[ "$2" -eq '0' ]]; then
        echo "Al doilea parametru este 0. Iesim..."
        exit 1
    else
        n="$(modulo "$1" "$2")"
        echo "$n"
    fi
    ;;
*)
    echo "Optiune invalida"
    exit 1
    ;;

    esac
}

meniu "$1" "$2"
