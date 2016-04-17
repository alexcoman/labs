#!/bin/bash

#Author:Spinu Marius
#Description: Simulating a `return to parents directory` of a directory

Up ()
{
    for ((i=1;i<="$1";i++)); do
        cd ../
    done
    exec /bin/bash
}


menu ()
{

    if [[ $# -ne 1 ]]; then
        echo "One parameter only"
    else
        if [[ "$1" -gt 0 ]]; then
            Up "$1"
        else
            echo "Only positive numbers"
        fi
    fi
}

menu "$1"
