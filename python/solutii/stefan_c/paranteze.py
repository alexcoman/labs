"""
    - []        este bine
    - []()      este bine
    - [()()]    este bine
    - ][        nu este bine
    - (][][)    nu este bine
    - [)]()[(]  nu este bine
"""


def este_corect(expresie):
    """
    Returns true or false if the expression is valid
    :param expresie: an expression formed out of parenthesis
    :return: read the doc
    """
    if len(expresie) % 2 != 0:
        return False
    opening_parenthesis = set('([')
    parenthesis = ([('(', ')'), ('[', ']')])
    stack = []
    for char in expresie:
        if char in opening_parenthesis:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            lastopened = stack.pop()
            if (lastopened, char) not in parenthesis:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
