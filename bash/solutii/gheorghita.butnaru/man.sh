#!/bin/bash

# Scrieti un script pentru cauta informatii in manualul unei comenzi
# ./man.sh nume_script informatie


f=\'\\$2\'
man "$1" | /bin/bash -c "grep -i $f"

