#!/bin/bash

#Autor: Teona Rusu
#Descriere: Script care contine functiile pentru math.sh

add ()
{
rez="$(($1 + $2))"
echo $rez
}
add 1 2

substract ()
{
rez="$(($1 - $2))"
echo $rez
}

substract 2 4

multiply ()
{
rez="$(($1 * $2))"
echo $rez
}

multiply 3 5

divide ()
{
rez="$(($1 / $2))"
echo $rez
}

divide 5 4

modulo ()
{
rez="$(($1 % $2))"
echo $rez
}

modulo 6 5
