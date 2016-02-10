#!/bin/bash


function incercare()
{
    local variabila=$(rm -rf "$1" >>/dev/null 2>&1)
    echo $?
}

incercare $1
