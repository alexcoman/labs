#!/bin/bash

# Scrieti un script care va ajuta sa mergeti prin directoare in sus
# Exemplu: 
# $ pwd
# /home/cgalan/folder1/folder2/folder3/folder4/folder5
# $ ./up.sh 3
# $ pwd
# /home/cgalan/folder1/folder2
jump="$1"

cd_funct() {
    for i in $(seq 1 "$jump"); do
        cd ..
        i="$i++"
    done
}


pwd
cd_funct
pwd
