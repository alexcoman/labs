#!/bin/bash

#Author: Spinu Marius 
#Description : Script that contains basic math functions

add ()
{
result="$(($1 + $2))"
echo $result
}

substract ()
{
result="$(($1 - $2))"
echo $result
}

multiply ()
{
result="$(($1 * $2))"
echo $result
}

divide ()
{
result="$(($1 / $2))"
echo $result
}

modulo ()
{
result="$(($1 % $2))"
echo $result
}
