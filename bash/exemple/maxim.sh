#!/usr/bin/env bash

# Scrieți o funcție care să determine maximul dintre două numere
# primite ca argument.

# Cerințe :
#   - Se va folosi structura if-else
#   - Se vor valida datele


function max {
    # check for numbers of arguments
    if [[ "$#" -lt 2 ]]; then
        echo "Functia primeste 2 parametri $# given " >&2;
        return 1;
    fi

    if [[ "$1" -gt "$2" ]]; then
        echo "$1";
    else
        echo "$2";
    fi
}
