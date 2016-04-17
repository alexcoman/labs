#!/bin/bash


    if [[ $# -ne 2 ]]; then
        echo "Insufficient parameters"
        exit 0
    fi

    if [[ $(which "$1") == '' ]]; then
        echo "Command not found"
    else
        man "$1" | grep "$2"
    fi
