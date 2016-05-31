"""
Scrieti o functie ce sa determine daca numarul
primit ca argument este o putere a lui 2.
"""


def power(number):
    """ Functia care verifica daca e putere a lui 2   """
    binar = bin(number)[2:]
    # binar = "{0:b}".format(number)
    if binar.count("1") == 1:
        print "Este putere a lui doi"
    else:
        print "Nu este putere a lui doi"

if __name__ == "__main__":
    power(int(raw_input("Gimme the number: ")))
