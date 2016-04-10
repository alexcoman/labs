#!/bin/bash

#Autor: Munteanu Stefan
#Descriere: functiile pentru math.sh


add(){
rez="$(($1+$2))"
echo $rez
}

substract(){
rez="$(($1-$2))"
echo $rez
}


multiply(){
rez="$(($1 * $2 ))"
echo $rez
}

divide(){
rez="$(($1/$2))"
echo $rez
}

modulo(){
rez= "$(($1 % $2))"
echo $rez
}

add 1 2
substract 2 1
multiply 2 3
divide 4 2
modulo 15 10
