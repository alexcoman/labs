#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=import-error
import argparse
import os
import subprocess
import glob
import logging
import yaml


def update(config):
    """Functia de update pentru sistem"""
    logging.info("Update Initiated")
    # Need update
    need_update = config['init'][0]
    need_update_value = need_update['need_update']['value']
    logging.info(">  Config values:")
    logging.info(">  Update needed? : {}".format(need_update_value))
    # Need upgrade
    need_upgrade = config['init'][1]
    need_upgrade_value = need_upgrade['need_upgrade']['value']
    logging.info(">  Upgrade needed? : {}".format(need_upgrade_value))
    if need_upgrade_value == True:
        need_upgrade_mode = need_upgrade['need_upgrade']['mode']
        logging.info(">  Upgrade mode? : %s", need_upgrade_mode)

    if need_update_value == True:
        need_update_command = "apt-get update"
        logging.info("I'm starting the update ( command used: {} )".format(need_update_command))
        logging.info("Updating the system...")
        subprocess.check_output(need_update_command+"; exit 0;", stderr=subprocess.STDOUT, shell=True)
        logging.info("Update finished successfully")
    if need_upgrade_value:
        if need_upgrade_mode == "force":
            need_upgrade_command = "apt-get upgrade -y"
            logging.info("I'm starting the upgrades ( command used: {} )".format(need_upgrade_command))
            logging.info("Upgrading the system...")
            subprocess.check_output(need_upgrade_command+"; exit 0;", stderr=subprocess.STDOUT, shell=True)
            logging.info("Upgrade finished successfully")
        else:
            need_upgrade_command = "apt-get upgrade"
            logging.info("I'm starting the upgrades ( command used: {} )".format(need_upgrade_command))
            logging.info("Upgrading the system...")
            subprocess.check_output(need_upgrade_command+"; exit 0;", stderr=subprocess.STDOUT, shell=True)
            logging.info("Upgrade finished successfully")


def create_user(config):
    """ Functia pentru a crea un user nou    """
    logging.info("Create a new user initiated")
    users = config['config']['user']
    logging.info(">  User configuration values:")
    for user in users:
        username = user
        expiratedate = users[user]['expiratedate']
        full_name = users[user]['full_name']
        group = users[user]['group']
        password = users[user]['password']
        logging.info(">  Username: {}".format(username))
        logging.info(">  Expirate date: {}".format(expiratedate))
        logging.info(">  Full Name: {}".format(full_name))
        logging.info(">  Group: {}".format(group))
        logging.info(">  Password: {}".format(password))

        logging.info("Creating of user {} is starting ...".format(username))

        logging.info("Checking if group {} is existing. If the group is not created will create one.".format(group))
        check_string = "groupdel: group"
        if check_string in str(
                subprocess.check_output("groupdel " + group + "; exit 0;", stderr=subprocess.STDOUT, shell=True)):
            subprocess.check_output("groupadd " + group + "; exit 0;", stderr=subprocess.STDOUT, shell=True)
            logging.info("Group {} added".format(group))
        else:
            logging.warning("The group {} is already created. No need to create one.".format(group))

        logging.info("Creating the user {} ...".format(username))

        if (username in str(
                subprocess.check_output("id " + username + "; exit 0;", stderr=subprocess.STDOUT, shell=True))):
            os.system("userdel {}".format(username))
            logging.warning(
                "The user {} is already there so I will delete one and recreate with given params".format(username))

        userstring = "useradd "
        if expiratedate != "":
            userstring = userstring + "-e \"{}\" ".format(expiratedate)
        if full_name != "":
            userstring = userstring + "-c \"{}\" ".format(full_name)
        if group != "":
            userstring = userstring + "-g \"{}\" ".format(group)
        if password != "":
            userstring = userstring + "-p \"{}\" ".format(password)
        userstring = userstring + username

        logging.info("User {} created".format(username))
        os.system(userstring)


def set_hostname(config):
    """ Functia pentru a seta un hostname anume """
    logging.info("Setting a new hostname")
    hostname = config['config']['hostname']
    current_hostname = subprocess.check_output("hostname; exit 0;", stderr=subprocess.STDOUT, shell=True)

    if hostname == current_hostname.strip():
        logging.info("No need to change the hostname ( hostname : {} ).".format(hostname))
    else:
        os.system("hostname {}".format(hostname))
        logging.info("Hostname changed ( From '{}' to '{}' )".format(hostname))


def create_directory(config):
    """ Functia pentru crearea unui director """
    logging.info("Creating a new directory for the service.")
    cfg = config['init'][2]
    path = cfg['download']['destination']
    os.system("mkdir -p {}".format(path))
    logging.info("The directory with the given path ( {} ) was created".format(path))


def download_script(config):
    """ Functia pentru crearea unui director """
    logging.info("Downloading the script.")
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']

    logging.info("Downloading the script to '{}'".format(path))
    logging.info("Download source: '{}'".format(source))

    os.chdir(path)
    os.system("wget {}".format(source))
    logging.info("File downloaded")


def install_script(config):
    """ Functia pentru instalare teamspeak server """
    logging.info("Installing the teamspeak3 server...")
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    for fisier in glob.glob("*.bz2"):
        os.system("bzip2 -d {}".format(fisier))
    for filee in glob.glob("*.tar"):
        os.system("tar xf {}".format(filee))
    os.system("rm -rf *.tar")
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source:
        folder_name = str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path + "/" + folder_name
        os.chdir(new_path)
        logging.info("I'm moving to {} ".format(new_path))
        print "You can now start server by re-executing the script and choosing start."

    else:
        logging.critical("Couldn't find the path for teamspeak 3 server in {}".format(path))
        revert_install(config)


def revert_install(config):
    """ Functia pentru a sterge tot """
    logging.info("Reverting everything.")

    delete_user = config['revert'][0]
    delete_user_method = delete_user['delete_user']['method']
    delete_user_user = delete_user['delete_user']['user']

    delete_path = config['revert'][1]
    delete_path_method = delete_path['delete_path']['method']
    delete_path_path = delete_path['delete_path']['path']

    reboot = config['revert'][2]
    reboot_method = reboot['reboot']['method']

    if delete_user_user != "":
        delete_user_command = "userdel"
        if delete_user_method == 'force':
            delete_user_command += " -f"
        delete_user_command = delete_user_command + " {}".format(delete_user_user)
        os.system(delete_user_command)
        logging.info("User '{}' deleted".format(delete_user_user))

    if delete_path_path != "":
        delete_path_command = "rm"
        if delete_path_method == "force":
            delete_path_command += " -rf"
        delete_path_command = delete_path_command + " {}".format(delete_path_path)
        os.system(delete_path_command)
        logging.info("Path '{}' deleted.".format(delete_path_path))

    if reboot_method == "none":
        logging.info("No reboot requesteds")
    elif reboot_method == "soft":
        reboot_command = "shutdown -r +1"
        logging.info("Server is restarting ( command used : {} )".format(reboot_command))
        os.system(reboot_command)


def install_server(config):
    update(config)
    create_user(config)
    set_hostname(config)
    create_directory(config)
    download_script(config)
    install_script(config)


def start_server(config):
    """ Functia pentru a pornit serverul """
    logging.info("Starting the server...")
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source:
        folder_name = str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path + "/" + folder_name
        os.chdir(new_path)
        start_command = "./ts3server_startscript.sh start"
        os.system(start_command)


def stop_server(config):
    """ Functia pentru a pornit serverul """
    logging.info("Stopping the server...")
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source:
        folder_name = str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path + "/" + folder_name
        os.chdir(new_path)
        start_command = "./ts3server_startscript.sh stop"
        os.system(start_command)


def restart_server(config):
    """ Functia pentru a pornit serverul """
    logging.info("Restarting the server...")
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source:
        folder_name = str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path + "/" + folder_name
        os.chdir(new_path)
        start_command = "./ts3server_startscript.sh restart"
        os.system(start_command)


def main(path):
    logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='[%(levelname)s][%(asctime)s] %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
            logging.info("===============================================")
            logging.info("Config file loaded")
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        logging.critical("Config file couldn't be opened.")
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("--install", help="Install Teamspeak3 Server", action='store_true')
    parser.add_argument("--start", help="Start Teamspeak3 Server", action='store_true')
    parser.add_argument("--stop", help="Stop Teamspeak3 Server", action='store_true')
    parser.add_argument("--restart",help="Restart Teamspeak3 Server", action='store_true')
    parser.add_argument("--delete", help="Revert Everything", action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    if args.install:
        install_server(config)
    if args.start:
        start_server(config)
    if args.stop:
        stop_server(config)
    if args.restart:
        restart_server(config)
    if args.delete:
        revert_install(config)
    if not args.install or not args.start or not args.stop or not args.restart or not args.delete :
        print "usage: init.py [-h] [--install] [--start] [--stop] [--restart] [--delete] [--version]"

if __name__ == "__main__":
    main("tuxy.config")
