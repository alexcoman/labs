#!/bin/bash

# 8.1. Scrieti un script care sa va ajute la scrierea programelor in C, care sa
# automatizeze ciclul: modificare-sursa -> compilare -> testare(executie). Scriptul trebuie se
# afiseze un meniu cu o serie de optiuni pentru utilizator. Pentru fiecare optiune trebuie
# scrisa o functie ( toate functiile trebuie scrise intr-un singur fisier).
# Optiuni meniu:
#   a) sa lanseze editorul de texte pentru fisierul fisier.c specificat ca parametru
# sau cerut de la linia de comanda;
#   b) sa lanseze compilatorul (fisierul executabil sa aiba numele fisier , deci fara
# sufixul .c); daca sunt erori de compilare (lucru observabil prin erorile de compilare afisate
# de compilator) sau warning-uri si sa le salveze intr-un fisier (fisier.err); fisierul de erori
# si executabilul se sterg la fiecare compilare;
#   c) sa afiseze continutul fisierului fisier.err daca sunt erori (exista fisierul si are
# dimensiunea > 0);
#   d) sa lanseze in executie programul ( afisare mesaj de eroare daca nu exista
# executabilul);
#   e) iesire din script.

print_menu() {
    echo "Introdu optiunea dorita urmata de tasta enter"
    echo " a - open editor "
    echo " b - compile code "
    echo " c - print compiler errors, if any"
    echo " d - run program"
    echo " e -  exit program"

    read option
}


open_file() {
    vim "$1"
}


compile() {
    if [ -e "$2" ];then
        rm "$2"
    fi
    if [ -e "$3" ];then
        rm "$3"
    fi

    gcc "$1" -o "$2" 2> "$3"
    if ! [ -s "$3" ];then
        printf "Compiled with no errors! \n\n\n\n\n"
    else
        printf "Compiled with errors! \n\n\n\n\n"
    fi
}


print_errs() {
    if [ -e "$1"  ] && [ -s "$1" ];then
        cat "$1"
    else
        printf "No errors, good job! \n\n\n\n\n"
    fi
}


run_program() {
    if [ -e "$1" ];then
        printf "Start ***************************\n\n"
        ./"$1"
    else
        printf "There is no file to execute! \n\n\n\n\n"
    fi

    printf "\nFinish **************************\n\n\n\n\n"
}


if [ "$1" == '' ] || ! [ -e "$1" ];then
    echo "Insert an file name"
    read filename
    if [ "$filename" == '' ];then
        echo "We need an filename"
        exit
    fi
else
    filename="$1"
fi


file=${filename%*.*}
file_err=$file".err"
clear
print_menu

while [ "$option" != "e" ];do
    clear
    case "$option" in
        a)
            open_file "$filename"
            ;;
        b)
            compile "$filename" "$file" "$file_err"
            ;;
        c)
            print_errs "$file_err"
            ;;
        d)
            run_program "$file"
            ;;
        e)
            exit
            ;;
        *)
            printf "Usage: %s {a|b|c|d|e}:\n\n\n\n\n" "$0"
    esac
    print_menu
done

