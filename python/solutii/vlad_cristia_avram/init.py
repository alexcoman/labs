"""Rezolvarea problemei de la test"""
# pylint: disable=import-error
from __future__ import print_function
import os
import shutil
import yaml


def download(config, log):
    """Functia de download"""
    log.write("S-a downloadat fisier\n")
    dict1 = config['before_install'][0]
    dest_url = dict1['download']['destination']
    with open(dest_url, 'w'):
        pass
    install(config, log)


def install(config, log):
    """Functia de instalare"""
    dictionar = config['install'][0]
    command = dictionar['run_script']['command']
    cwd = dictionar['run_script']['cwd']
    env_variables = dictionar['run_script']['env_variables']
    os.system("cd %s" % cwd)
    os.system(command)
    locals().update(env_variables)
    reboot(config, log)


def install_failed(config, log):
    """Functia pentru eventualitatea in care da gres instalarea"""
    log.write("Instalarea nu a avut succes\n")
    dictionar = config['install_failed'][0]
    delete_method = dictionar['delete']['method']
    path = dictionar['delete']['path']
    if delete_method:
        shutil.rmtree(path, True)
    log.write("Am sters fisierul %s\n" % path)
    dir2 = config['install_failed'][1]
    shutdown_method = dir2['shutdown']['method']
    log.write("Sistemul se va inchide\n")
    if shutdown_method == "hard":
        os.system("shutdown -s -f")
    else:
        os.system("shutdown -s")


def configurare(config, log):
    """Functia de configurare"""
    log.write("Se realizeaza configurarile\n")
    users = config['config']['users']
    for user in users:
        log.write("S-a adaugat userul %s\n" % user)
        os.system("adduser -D %s" % user)
        date = config['config']['users'][user]['expiredate']
        print(date)
        os.system("adduser -e %s" % date)
        primary_group = config['config']['users'][user]['primary-group']
        os.system("adduser -g %s" % primary_group)
        groups = config['config']['users'][user]['groups']
        os.system("adduser -G %s" % groups)
        password = config['config']['users'][user]['password']
        os.system("adduser -p %s" % password)
        log.write("S-a configurat userul %s\n" % user)
    files = config['config']['write_files']
    for fisier in files:
        path = config['config']['write_files'][fisier]['path']
        content = config['config']['write_files'][fisier]['content']
        encoding = config['config']['write_files'][fisier]['encoding']
        permission = config['config']['write_files'][fisier]['permissions']
        filename = fisier
        os.system("cd %s" % path)
        os.system("touch %s" % filename)
        os.system("echo %s >> %s" % (content, filename))
        os.system("recode %s %s" % (encoding, filename))
        os.system("chmod %s %s" % (permission, filename))
        log.write("S-a scris fisierul %s\n" % filename)
    download(config, log)


def reboot(config, log):
    """Funcia de reboot"""
    log.write("S-a terminat procedura de instalare\n")
    dictionar = config['after_install'][0]
    method = dictionar['reboot']['method']
    log.write("Sistemul se va restarta\n")
    if method == "soft":
        os.system("shutdown -r")
    else:
        os.system("shutdown -r -f")


def main(path):
    """Citim fisierul de configurare."""
    log = open("build.log", "w")
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
            log.write("Am deschis fisierul Config\n")
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        log.write("Nu am putut citi datele din fisierul de configurare\n")
        return
    configurare(config, log)


if __name__ == "__main__":
    main("tuxy.config")
