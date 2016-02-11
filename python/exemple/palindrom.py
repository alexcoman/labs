#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Scrieți o funcție ce să determine dacă șirul de caractere
primit ca argument este palindrom.
"""


def palindrom(sir):
    """Funcție ce determină dacă șirul primit este palindrom."""
    return sir == sir[::-1]


if __name__ == "__main__":
    assert not palindrom("python")
    assert palindrom("radar")
    assert not palindrom("palindrom")
