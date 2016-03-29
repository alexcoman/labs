#!/usr/bin/env bash

# Scrieți o funcție care să determine maximul dintre două numere
# primite ca argument.

# Cerințe :
#   - Se va folosi structura if-else


function max {
    first_argument="$1"
    second_argument="$2"

    if [[ "$first_argument" -gt "$second_argument" ]]; then
        echo "$first_argument"
    else
        echo "$second_argument"
    fi
}

# Teste
echo "Maximul dintre 1 și 2 : $(max 1 2)"
echo "Maximul dintre 5 și 6 : $(max 5 6)"
echo "Maximul dintre 1 și 1 : $(max 1 1)"
