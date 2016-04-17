#!/bin/bash

    if [[ $# -ne 2 ]]; then
        echo "Insufficient parameters"
        exit 0
    else
        if [[  -d "$1" && -d "$2" ]]; then
            diff --brief -r "$1" "$2" > differences.txt
            if [[ $(stat -c%s differences.txt) -le 0 ]]; then
                echo "Nu sunt diferente , deci sunt egale"
            else
                echo "Exista diferente"
            fi

            rm differences.txt
        else
            echo "Invalid parameters"
        fi
    fi
