#!/bin/bash

#Author: Spinu Marius
#Description: Main file for options.sh

    if [[ $# -ne '1' ]]; then
        echo "You must have one parameter"
        exit 1
    fi

    if [[ -f "$1" ]]; then
        if [[ "${1:${#1} - 2}" != ".c" ]]; then
            echo "File invalid"
            exit 1
        fi
    else
        echo "Source file not found"
        exit 1
    fi

    if [[ ! -f options.sh ]]; then
        echo "Options not found"
        exit 1
    else
        . options.sh
    fi

    menu ()
    {
    not_exit=1
    while [[ "$not_exit" ]]; do
    echo ""
    echo "Menu:"
    echo -e '\t' 1.Modify
    echo -e '\t' 2.Compile
    echo -e '\t' 3.View errors
    echo -e '\t' 4.Run
    echo -e '\t' 5.Exit

    read -p 'Option ' opt

    case "$opt" in
    5)
    exit 0;
    ;;
    1)
    modify "$1"
    ;;
    2)
    compile "$1"
    ;;
    3)
    show_err "$1"
    ;;
    4)
    run "$1"
    ;;

    *)
    echo "Invalid option"
    exit 1;
    esac
    done
    }

    menu "$1"
