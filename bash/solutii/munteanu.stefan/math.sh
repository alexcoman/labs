#!/bin/bash

#Autor: Munteanu Stefan
#Descriere: Fisier de baza pentru math.

if [[ $# -ne '2' ]]; then
    echo "Fisierul primeste 2 parameti. Exemplu: ./$0 10 20"
    exit 1
fi

if [[ ! -f script.sh  ]]; then
    echo"Fisierul cu functii nu exista"
    exit 1
else
    . script.sh
fi

meniu(){
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
   n="$(divide "$1" "$2")"
   echo "$n"
  ;;
  5)
   n="$(modulo "$1" "$2")"
   echo "$n"
  ;;
  *)
   echo "Nu e bun inputul"
   exit 1;
  esac
}

meniu $1 $2
