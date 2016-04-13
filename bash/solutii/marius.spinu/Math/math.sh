#!/bin/bash

#Author : Spinu Marius
#Description : Main file for math exercises.

    if [[ $# -ne '2' ]]; then
        echo "Not enough params"
        exit 1
    fi

    if [[ ! -f script.sh ]]; then
        echo "File not found"
        exit 1
    else
        . script.sh
    fi

    meniu ()
    {
    echo "Menu:"
    echo -e '\t' 1:Add
    echo -e '\t' 2:Substract
    echo -e '\t' 3:Multiply
    echo -e '\t' 4:Divide
    echo -e '\t' 5:Modulo

    read -p 'Option ' opt

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
        echo "Second parameter is 0"
        exit 1;
    else
        n="$(divide "$1" "$2")"
        echo "$n"
    fi
    ;;
    5)
    if [[ "$2" -eq '0' ]]; then
        echo "Second parameter is 0"
    else
        n="$(modulo "$1" "$2")"
        echo "$n"
    fi
    ;;

    *)
    echo "Invalid Option"
    exit 1;
    esac
    }
    meniu "$1" "$2"
