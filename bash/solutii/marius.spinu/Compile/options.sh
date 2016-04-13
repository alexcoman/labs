#!/bin/bash

#Author: Spinu Marius
#Description: Script that contains all functionalities for compile.sh

modify ()
{
nano "$1"
}

compile ()
{

if [[ -f "${1::-2}".err ]]; then #daca exista fisierul cu erori il stergem
rm "${1::-2}".err
fi

if [[ -f "${1::-2}" ]]; then #analog pentru executabil
rm "${1::-2}"
fi

g++ "$1" -o "${1::-2}" 2>"${1::-2}".err #compilam -eliminam ultimele 2 char. (fara .c)

if [[ $(stat -c%s "${1::-2}".err) <=0 ]]; then #daca fisierul cu erori este gol , il stergem
rm "${1::-2}".err
fi

}

show_err ()
{
if [[ -f "${1::-2}".err ]]; then
cat "${1::-2}".err
else
echo "File not found"
fi
}

run ()
{
if [[ -f "${1::-2}" ]]; then
./"${1::-2}"
else
echo "Executable not found"
fi
}

terminate ()
{
exit 1
}
