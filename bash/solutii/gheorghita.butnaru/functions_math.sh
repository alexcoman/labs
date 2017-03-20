#!/bin/bash

function add {
    echo $(($1 + $2))
}

function sub {
    echo $(($1 - $2))
}

function mult {
    echo $(($1 * $2))
}

function div {
    echo $(($1 / $2))
}

function mod {
    echo $(($1 % $2))
}
