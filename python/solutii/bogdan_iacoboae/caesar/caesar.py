# coding=utf-8

# from __future__ import print_function
"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.
Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.
Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""


def afla_pasul(mesaj):
    """ Afla pasul encodarii """
    first_letter = 'a'
    my_letter = mesaj[0]
    return ord(my_letter) - ord(first_letter)


def real_letter(character, key):
    """ Afla caracterul """
    if character.isalpha():
        character = ord(character)-key
        if character < ord('a'):
            character = ord('z') - abs(ord('a') - character) + 1
        return chr(character)
    else:
        return character


def decripteaza_mesajul(mesaj, fisier):
    """ Decriptarea mesajului """
    key = afla_pasul(mesaj)
    puncte = 0.
    for index in mesaj:
        if index == ".":
            if puncte == 1:
                print ".\n"
                fisier.write("\n")
            else:
                puncte = puncte + 1
                print ".",
                fisier.write(".")
        else:
            print real_letter(index, key),
            fisier.write(real_letter(index, key))


def main():
    """ Main function docstring """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        towrite = open("../../../date_iesire/mesaje.decodat", "w")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obtine mesajele."
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj, towrite)

if __name__ == "__main__":
    main()
