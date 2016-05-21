#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Aplicația tuxy-init."""

# pylint: disable=import-error

from __future__ import print_function

# Notes: Pentru a instala bibleoteca yaml trebuie să rulați
#        următoarea comandă: pip install pyaml

import yaml


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return

    print(config)


if __name__ == "__main__":
    main("../../date_intrare/tuxy.config")
