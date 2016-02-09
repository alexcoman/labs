"""
Implement paint fill function for a given matrix
"""
from __future__ import print_function


def matrix_print(rows, columns, image):
    """
    Prints a matrix
    :param rows: rows of the matrix
    :param columns: cols of the matrix
    :param image: the image/matrix
    :return: a printed image/matrix
    """
    for i in xrange(0, rows):
        for j in xrange(0, columns):
            print (image[i][j], end="")
        print()


def umple(imagine, punct):
    """
    Fills the image with * characters
    :param imagine: the image/matrix
    :param punct: the position from where to start filling
    :return: the filled image
    """
    positionx, positiony = punct[0], punct[1]
    if imagine[positionx][positiony] == '*':
        return
    imagine[positionx][positiony] = '*'
    if positiony < (len(imagine[0]) - 1):
        umple(imagine, (positionx, positiony + 1))
    if positiony >= 1:
        umple(imagine, (positionx, positiony - 1))
    if positionx < (len(imagine) - 1):
        umple(imagine, (positionx + 1, positiony))
    if positionx >= 1:
        umple(imagine, (positionx - 1, positiony))
    return imagine


def main():
    """
    The main function
    :return: a printed filled image
    """
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple(imaginea, (1, 3))
    umple(imaginea, (5, 11))
    matrix_print(len(imaginea), len(imaginea[0]), imaginea)


if __name__ == "__main__":
    main()
