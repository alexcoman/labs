#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Problema unic."""

from __future__ import print_function


def gaseste_unic(istoric):
    """unic"""
    result = istoric.pop()
    for numar in istoric:
        result = result ^ numar
    return result


if __name__ == "__main__":
    assert gaseste_unic([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic([1, 1, 1, 2, 2]) == 1
