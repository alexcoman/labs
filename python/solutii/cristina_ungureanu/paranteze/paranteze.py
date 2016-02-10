#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Stabileste daca o expresie de paranteze este corecta."""


def este_corect(expresie):
    """Apreciaza corectitudinea expresiei."""
    memo = []
    for _, val in enumerate(expresie):
        if val not in '([)]':
            return False
        if val == '(' or val == '[':
            memo.append(val)
        if val == ')':
            if memo and memo[len(memo)-1] == '(':
                memo.pop()
            else:
                return False
        if val == ']':
            if memo and memo[len(memo)-1] == '[':
                memo.pop()
            else:
                return False
    return not memo


if __name__ == "__main__":
    assert not este_corect("[9]")
    assert not este_corect("[")
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
