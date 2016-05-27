"""
Acest modul pune la dispozitie o functie cu ajutorul careia pot fi
sincronizate 2 directoare, bidirectional - pentru orice schimbare in oricare
din cele 2 directoare, schimbarea respectiva conduce la o aceeasi schimbare
in celalalt director.
Sincronizarea are loc pe tot subarborele asociat fiecarui director.
"""

import sys
import os
import os.path
import shutil
import time
import filecmp


def copy_all(file_list, src, dest):

    """
    Functia copiaza toate Fisierele / Directoarele (impreuna cu arborele
    asociat directorului) ale caror nume sunt specificate in file_list, ce se
    gasesc in directorul src, catre directorul dest.
    """

    for lfile in file_list:
        lfile_path = os.path.join(src, os.path.basename(lfile))
        if os.path.isdir(lfile_path):
            shutil.copytree(lfile_path,
                            os.path.join(dest, os.path.basename(lfile)))
            print "Copied directory {} from {} to {}.".format(
                os.path.basename(lfile), os.path.basename(src),
                os.path.basename(dest))
        else:
            shutil.copy2(lfile_path, dest)
            print "Copied file {} from {} to {}.".format(
                os.path.basename(lfile), os.path.basename(src),
                os.path.basename(dest))


def check(dir1, dir2):

    """
    Functia verifica si inregistreaza modificarile din directoarele
    dir1 si dir2 dupa care, in dependenta de modificari, actioneaza intr-un
    mod sau altul.
    Pentru toate directoarele comune - cu acelasi nume de director, este
    apelata recursiv aceasta functie;
    Pentru toate numele de fisierele ce apar doar in dir1, se copiaza in dir2;
    Similar pentru dir2;
    Pentru toate fisierele comune - cu acelasi nume de fisier, dar cu continut
    este suprascris fisierul cu ultima data a modificarii cea mai recenta;
    """

    comparison = filecmp.dircmp(dir1, dir2)
    if comparison.common_dirs:
        for ldir in comparison.common_dirs:
            check(os.path.join(dir1, ldir), os.path.join(dir2, ldir))
    if comparison.left_only:
        copy_all(comparison.left_only, dir1, dir2)
    if comparison.right_only:
        copy_all(comparison.right_only, dir2, dir1)
    dir1_newer = []
    dir2_newer = []
    if comparison.diff_files:
        for lfile in comparison.diff_files:
            mtime1 = os.stat(os.path.join(dir1, lfile)).st_mtime
            mtime2 = os.stat(os.path.join(dir2, lfile)).st_mtime
            if mtime1 > mtime2:
                dir1_newer.append(lfile)
            else:
                dir2_newer.append(lfile)
    copy_all(dir1_newer, dir1, dir2)
    copy_all(dir2_newer, dir2, dir1)


def synchronize(dir1, dir2, ptime):

    """
    Functia porneste procesul de sincronizare a directoarelor dir1 si dir2.
    Din ptime in ptime va face cate o verificare pentru modificari in cele
    doua directoare si va actiona corespunzator pentru fiecare modificare.
    """

    print "   Synchronization between {} and {} was started! ({})\n".format(
        os.path.basename(dir1), os.path.basename(dir2), time.ctime())
    print " Source Directory Path: {}".format(dir1)
    print " Destination Directory Path: {}".format(dir2)
    print
    while True:
        print " Checking ... "
        check(dir1, dir2)
        print " Checking ... DONE\n"
        time.sleep(ptime)


if __name__ == "__main__":
    print

    if len(sys.argv) != 4:
        print "Too many/much arguments!"
        print " Usage: python {} <dir1> <dir2> <time>".format(sys.argv[0])
        exit()

    if not os.path.isdir(os.path.join(sys.argv[1])):
        print "{} is not a directory!".format(sys.argv[1])
        exit()

    if not os.path.isdir(os.path.join(sys.argv[2])):
        print "{} is not a directory!".format(sys.argv[2])
        exit()

    try:
        PTIME = int(sys.argv[3])
    except ValueError:
        print "{} is not an integer!".format(sys.argv[3])
        exit()

    synchronize(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]),
                PTIME)
