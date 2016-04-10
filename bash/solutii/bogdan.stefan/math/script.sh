#!/bin/bash

#Author: Bogdan Stefan
#Descriere: Script care contine functiile pentru math.sh

add ()
{
rez="$(($1 + $2))"
echo $rez
}

substract ()
{
rez="$(($1 - $2))"
echo $rez
}

multiply ()
{
rez="$(($1 * $2))"
echo $rez
}

divide ()
{
rez="$(($1 / $2))"
echo $rez
}

modulo ()
{
rez="$(($1 % $2))"
echo $rez
}
