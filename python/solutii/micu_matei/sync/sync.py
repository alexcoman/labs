#!/usr/bin/env python
"""
Syncronizam doua fisiere
"""
from __future__ import print_function
import os
import argparse
import shutil
from functii_auxiliare import get_hash
from functii_auxiliare import get_last_edit
from functii_auxiliare import write_sync_file
from functii_auxiliare import read_sync_file
from functii_auxiliare import make_dirs
from functii_auxiliare import copy_r
from functii_auxiliare import get_same_file

# standard keys in dict
FULL_PATH = "fullPath"
MD5 = "md5"
BASE_DIR = "baseDir"
LAST_EDIT = "lastEdit"
IS_FILE = "isFile"


def parse_directory(base_dir, path, prefix):
    """ returneaza un dict in care cheile sunt pathuri relative la
    <path>-ul primit ca parametru, fiecare valoare este alt dict
    cu mai multi parametri, cum ar fi :
        - full_path
        - md5 ( daca este fisier  )
        - base_dir( directorul in care sincronizam  )
        - last_modified_date ( ultima data cand a fost modifica
                               daca e fisier )
        - is_file ( True / False )
    """

    if os.path.exists(path) and os.path.isdir(path):
        info = {}
        for item in os.listdir(path):
            full_path_info = os.path.join(path, item)
            relative_path_info = os.path.join(prefix, item)
            if os.path.isfile(full_path_info):
                info[relative_path_info] = {
                    FULL_PATH: full_path_info,
                    MD5: get_hash(full_path_info),
                    BASE_DIR: base_dir,
                    LAST_EDIT: get_last_edit(full_path_info),
                    IS_FILE: True
                    }
            elif os.path.isdir(full_path_info):
                info[relative_path_info] = {
                    FULL_PATH: full_path_info,
                    MD5: get_hash(full_path_info),
                    BASE_DIR: base_dir,
                    LAST_EDIT: get_last_edit(full_path_info),
                    IS_FILE: False
                    }
                info_sub = parse_directory(base_dir,
                                           full_path_info, relative_path_info)
                info.update(info_sub)
        return info
    else:
        return {}


def sync_new_files(info_a, path_a, info_b, path_b):
    """ Sincronizeaza fisierele noi din fisierul A in fisierul B,
    folosind informatiile fin info_a si info_b ."""
    for item in info_a:
        detalii_item = info_a[item]
        full_path_item_in_a = os.path.join(path_a, item)
        full_path_item_in_b = os.path.join(path_b, item)

        if item not in info_b:
            if detalii_item[IS_FILE]:
                copy_r(full_path_item_in_a, full_path_item_in_b)
            else:
                make_dirs(full_path_item_in_b)


def sync_deleted_files(info_a, info_b, path_b):
    """ Sincronizam fisierele deletate din fisierul A in fisierul B,
    folosind informatiile din info_a, info_b si fisierele de
    sincronizare daca acestea exista

    Eliminam fisierele din B care au fost eliminate in A, daca acestea
    existau deja in B inainte """
    sync_b = read_sync_file(path_b)

    if not sync_b:
        return

    for item in info_b:
        if (item not in info_a) and (item in sync_b):
            detalii_item = info_b[item]
            if detalii_item[IS_FILE]:
                os.remove(detalii_item[FULL_PATH])
            else:
                shutil.rmtree(detalii_item[FULL_PATH])


def sync_moved_files(info_a, info_b, path_b):
    """ Verifica daca un fisier a fost mutat """

    for item in info_a:
        if info_a[item][IS_FILE]:
            if item not in info_b:
                old_file = get_same_file(info_a[item], info_b)
                if old_file:
                    old_file = os.path.join(path_b, old_file)
                    new_path = os.path.join(path_b, item)
                    shutil.move(old_file, new_path)


def sync_modified_files(info_a, info_b):
    """ syncronizam fisierele modificate din A in B"""
    for item in info_a:
        if item in info_b:
            file_a = info_a[item]
            file_b = info_b[item]
            if file_a[MD5] != file_b[MD5]:
                if file_a[LAST_EDIT] > file_b[LAST_EDIT]:
                    os.remove(file_b[FULL_PATH])
                    shutil.copy(file_a[FULL_PATH], file_b[FULL_PATH])
                else:
                    os.remove(file_a[FULL_PATH])
                    shutil.copy(file_b[FULL_PATH], file_a[FULL_PATH])


def parse():
    """ parseaza argumentele primite ca parametri """
    args = argparse.ArgumentParser()
    args.add_argument('firstDir', type=str, help="Primul fisier")
    args.add_argument('secondDir', type=str, help="Al doilea fisier")

    args = args.parse_args()
    return args


def sync(path_a, path_b):
    """ syncronizeaza fisierele din cele doua directoare """
    # modified files
    info_a = parse_directory(path_a, path_a, "")
    info_b = parse_directory(path_b, path_b, "")
    sync_modified_files(info_a, info_b)
    # sync_modified_files(info_b, info_a)

    # moved files
    info_a = parse_directory(path_a, path_a, "")
    info_b = parse_directory(path_b, path_b, "")
    sync_moved_files(info_a, info_b, path_b)
    sync_moved_files(info_b, info_a, path_a)

    # delete files
    info_a = parse_directory(path_a, path_a, "")
    info_b = parse_directory(path_b, path_b, "")
    sync_deleted_files(info_a, info_b, path_b)
    sync_deleted_files(info_b, info_a, path_a)

    # new files
    info_a = parse_directory(path_a, path_a, "")
    info_b = parse_directory(path_b, path_b, "")
    sync_new_files(info_a, path_a, info_b, path_b)
    sync_new_files(info_b, path_b, info_a, path_a)

    # rescriem fisierele de sincronizare cu ultimele valori
    info_a = parse_directory(path_a, path_a, "")
    info_b = parse_directory(path_b, path_b, "")
    write_sync_file(path_a, info_a)
    write_sync_file(path_b, info_b)


def check_path(path):
    """ verifica daca path exista si este valida"""

    if not os.path.exists(path):
        print("EROARE: ", path, " trebuie sa existe")
        return False
    elif not os.path.isdir(path):
        print("EROARE: ", path, " trebuie sa existe")
        return False
    return True


def main():
    """ syncronizeaza pentru todeauna """
    args = parse()
    path_a = os.path.abspath(args.firstDir)
    path_b = os.path.abspath(args.secondDir)

    check_path(path_a)
    check_path(path_b)

    while True:
        sync(path_a, path_b)


if __name__ == "__main__":
    main()
