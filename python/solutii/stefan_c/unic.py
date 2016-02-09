"""
primeste o lista cu elemente numerice
si returneaza elem nu este duplicat.
"""


def gaseste(istoric):
    """
    :param istoric: istoric is the list of elements
    :return: the unique element from the list
    """
    unic = istoric[0]
    for i in xrange(1, len(istoric)):
        unic ^= istoric[i]
    return unic


if __name__ == "__main__":
    gaseste([1, 2, 3, 2, 1])
    gaseste([1, 1, 1, 2, 2])
