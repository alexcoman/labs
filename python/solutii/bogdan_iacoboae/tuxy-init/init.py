#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=import-error

import yaml
import datetime
import os
import popen2
import commands
import subprocess
import urllib
import glob


def update(config, log):
    """Functia de update pentru sistem"""
    log.write("[{:%Y-%m-%d %H:%M:%S}] Update Initiated \n".format(datetime.datetime.now()))
    # Need update
    need_update = config['init'][0]
    need_update_value = need_update['need_update']['value']
    log.write(">  Config values: \n")
    log.write(">  Update needed? : {}\n".format(need_update_value))
    # Need upgrade
    need_upgrade = config['init'][1]
    need_upgrade_value = need_upgrade['need_upgrade']['value']
    log.write(">  Upgrade needed? : {}\n".format(need_upgrade_value))
    if need_upgrade_value == True:
        need_upgrade_mode = need_upgrade['need_upgrade']['mode']
        log.write(">  Upgrade mode? : {}\n".format(need_upgrade_mode))

    if need_update_value == True:
        need_update_command = "apt-get update"
        log.write(
            "[{:%Y-%m-%d %H:%M:%S}] I'm starting the update ( command used: {} )\n".format(datetime.datetime.now(),
                                                                                           need_update_command))
        os.system(need_update_command)
        log.write("[{:%Y-%m-%d %H:%M:%S}] Update finished successfully\n".format(datetime.datetime.now(),
                                                                                 need_update_command))
    if need_upgrade_value == True:
        if need_upgrade_mode == "force":
            need_upgrade_command = "apt-get upgrade -y"
            log.write("[{:%Y-%m-%d %H:%M:%S}] I'm starting the upgrades ( command used: {} )\n".format(
                datetime.datetime.now(), need_upgrade_command))
            os.system(need_upgrade_command)
            log.write("[{:%Y-%m-%d %H:%M:%S}] Upgrade finished successfully\n".format(datetime.datetime.now(),
                                                                                      need_update_command))
        else:
            need_upgrade_command = "apt-get upgrade"
            log.write("[{:%Y-%m-%d %H:%M:%S}] I'm starting the upgrades ( command used: {} )\n".format(
                datetime.datetime.now(), need_upgrade_command))
            os.system(need_upgrade_command)
            log.write("[{:%Y-%m-%d %H:%M:%S}] Upgrade finished successfully\n".format(datetime.datetime.now(),
                                                                                      need_update_command))

    log.write("\n\n")



def create_user(config, log):
    """ Functia pentru a crea un user nou    """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Create a new user initiated \n".format(datetime.datetime.now()))
    users = config['config']['user']
    log.write(">  User configuration values: \n")
    for user in users:
        username = user
        expiratedate = users[user]['expiratedate']
        full_name = users[user]['full_name']
        group = users[user]['group']
        password = users[user]['password']
        log.write(">  Username: {} \n".format(username))
        log.write(">  Expirate date: {} \n".format(expiratedate))
        log.write(">  Full Name: {} \n".format(full_name))
        log.write(">  Group: {} \n".format(group))
        log.write(">  Password: {} \n".format(password))

        log.write("[{:%Y-%m-%d %H:%M:%S}] Creating of user {} is starting ...\n".format(datetime.datetime.now(),username))

        log.write("[{:%Y-%m-%d %H:%M:%S}] Checking if group {} is existing. If the group is not created will create one. \n".format(datetime.datetime.now(),group))
        check_string = "groupdel: group"
        if check_string in str(subprocess.check_output("groupdel " + group + "; exit 0;", stderr=subprocess.STDOUT, shell=True)):
            os.system("groupadd {}".format(group))
            log.write("[{:%Y-%m-%d %H:%M:%S}] Group {} added. \n".format(datetime.datetime.now(),group))
        else:
            log.write("[{:%Y-%m-%d %H:%M:%S}] The group {} is already created. No need to create one. \n".format(datetime.datetime.now(),group))

        log.write("[{:%Y-%m-%d %H:%M:%S}] Creating the user {} ... \n".format(datetime.datetime.now(),username))

        if ( username in str(subprocess.check_output("id " + username + "; exit 0;", stderr=subprocess.STDOUT, shell=True))) :
            os.system("userdel {}".format(username))
            log.write("[{:%Y-%m-%d %H:%M:%S}] The user {} is already there so I will delete one and recreate with given params'. \n".format(datetime.datetime.now(),username))

        userstring = "useradd "
        if expiratedate != "" :
            userstring = userstring + "-e \"{}\" ".format(expiratedate)
        if full_name != "":
            userstring = userstring + "-c \"{}\" ".format(full_name)
        if group != "":
            userstring = userstring + "-g \"{}\" ".format(group)
        if password != "":
            userstring = userstring + "-p \"{}\" ".format(password)
        userstring = userstring + username

        log.write("[{:%Y-%m-%d %H:%M:%S}] User {} created. \n".format(datetime.datetime.now(),username))
        os.system(userstring)
        log.write("\n\n")


def set_hostname(config,log):
    """ Functia pentru a seta un hostname anume """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Setting a new hostname. \n".format(datetime.datetime.now()))
    hostname= config['config']['hostname']
    current_hostname =  subprocess.check_output("hostname; exit 0;", stderr=subprocess.STDOUT, shell=True)

    if hostname == current_hostname.strip() :
        log.write("[{:%Y-%m-%d %H:%M:%S}] No need to change the hostname ( hostname : {} ). \n".format(datetime.datetime.now(), hostname))
    else:
        os.system("hostname {}".format(hostname))
        log.write("[{:%Y-%m-%d %H:%M:%S}] Hostname changed ( From '{}' to '{}' ). \n".format(datetime.datetime.now(),current_hostname.strip(),hostname))
    log.write("\n\n")


def create_directory(config,log):
    """ Functia pentru crearea unui director """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Creating a new directory for the service. \n".format(datetime.datetime.now()))
    cfg = config['init'][2]
    path = cfg['download']['destination']
    os.system("mkdir -p {}".format(path))
    log.write("[{:%Y-%m-%d %H:%M:%S}] The directory with the given path ( {} ) was created. \n".format(datetime.datetime.now(),path))
    log.write("\n\n")

def download_script(config,log):
    """ Functia pentru crearea unui director """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Downloading the script. \n".format(datetime.datetime.now()))
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']

    log.write("[{:%Y-%m-%d %H:%M:%S}] Downloading the script to '{}'. \n".format(datetime.datetime.now(),path))
    log.write("[{:%Y-%m-%d %H:%M:%S}] Download source : '{}'. \n".format(datetime.datetime.now(),source))

    os.chdir(path)
    os.system("wget {}".format(source))
    log.write("[{:%Y-%m-%d %H:%M:%S}] File downloaded. \n".format(datetime.datetime.now()))
    log.write("\n\n")

def install_script(config,log):
    """ Functia pentru instalare teamspeak server """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Installing the teamspeak3 server \n".format(datetime.datetime.now()))
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    for file in glob.glob("*.bz2"):
        os.system("bzip2 -d {}".format(file))
    for filee in glob.glob("*.tar"):
        os.system("tar xf {}".format(filee))
    os.system("rm -rf *.tar")
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source :
        folder_name=str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path+ "/" + folder_name
        os.chdir(new_path)
        log.write("[{:%Y-%m-%d %H:%M:%S}] I'm moving to {} \n".format(datetime.datetime.now(),new_path))
        print "You can now start server by re-executing the script and choosing start."

    else:
        log.write("[{:%Y-%m-%d %H:%M:%S}] Couldn't find the path for teamspeak3 server in {} \n".format(datetime.datetime.now(),path))
        revert_install(config,log)


def revert_install(config,log):
    """ Functia pentru a sterge tot """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Reverting everything. \n".format(datetime.datetime.now()))

    delete_user = config['revert'][0]
    delete_user_method = delete_user['delete_user']['method']
    delete_user_user = delete_user['delete_user']['user']

    delete_path = config['revert'][1]
    delete_path_method = delete_path['delete_path']['method']
    delete_path_path=delete_path['delete_path']['path']

    reboot = config['revert'][2]
    reboot_method = reboot['reboot']['method']

    if delete_user_user != "" :
        delete_user_command = "userdel"
        if delete_user_method == 'force' :
            delete_user_command = delete_user_command + " -f"
        delete_user_command = delete_user_command + " {}".format(delete_user_user)
        os.system(delete_user_command)
        log.write("[{:%Y-%m-%d %H:%M:%S}] User '{}' deleted. \n".format(datetime.datetime.now(),delete_user_user))

    if delete_path_path != "" :
        delete_path_command = "rm"
        if delete_path_method == "force" :
            delete_path_command = delete_path_command + " -rf"
        delete_path_command = delete_path_command + " {}".format(delete_path_path)
        os.system(delete_path_command)
        log.write("[{:%Y-%m-%d %H:%M:%S}] Path '{}' deleted \n".format(datetime.datetime.now(),delete_path_path))

    if reboot_method == "none" :
        log.write("[{:%Y-%m-%d %H:%M:%S}] No reboot requested \n".format(datetime.datetime.now()))
    elif reboot_method == "soft" :
        reboot_command = "shutdown -r +1"
        log.write("[{:%Y-%m-%d %H:%M:%S}] Server is restarting ( command used : {} ) \n".format(datetime.datetime.now(),reboot_command))
        os.system(reboot_command)

def install_server(config,log):
    update(config,log)
    create_user(config, log)
    set_hostname(config,log)
    create_directory(config,log)
    download_script(config,log)
    install_script(config,log)

def start_server(config,log):
    """ Functia pentru a pornit serverul """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Starting server...\n".format(datetime.datetime.now()))
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source :
        folder_name=str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path+ "/" + folder_name
        os.chdir(new_path)
        start_command= "./ts3server_startscript.sh start"
        os.system(start_command)

def stop_server(config,log):
    """ Functia pentru a pornit serverul """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Starting server...\n".format(datetime.datetime.now()))
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source :
        folder_name=str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path+ "/" + folder_name
        os.chdir(new_path)
        start_command= "./ts3server_startscript.sh stop"
        os.system(start_command)

def restart_server(config,log):
    """ Functia pentru a pornit serverul """
    log.write("[{:%Y-%m-%d %H:%M:%S}] Starting server...\n".format(datetime.datetime.now()))
    cfg = config['init'][2]
    path = cfg['download']['destination']
    source = cfg['download']['source']
    os.chdir(path)
    if str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip() in source :
        folder_name=str(subprocess.check_output("ls; exit 0;", stderr=subprocess.STDOUT, shell=True)).strip()
        new_path = path+ "/" + folder_name
        os.chdir(new_path)
        start_command= "./ts3server_startscript.sh restart"
        os.system(start_command)

def main(path):
    log = open("logs.log", "w")
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
            log.write("[{:%Y-%m-%d %H:%M:%S}] Config file loaded \n".format(datetime.datetime.now()))
            log.write(" \n")
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        log.write("[{:%Y-%m-%d %H:%M:%S}] Config file couldn't be opened \n".format(datetime.datetime.now()))
        log.write(" \n")
        return

    input = raw_input("What do you want to do ? : (install a new server, start the server, stop the server, restart the server, delete the server)\n Available commands: install,start,stop,delete \n")
    if( input.strip() == "install"):
        install_server(config,log)
    elif( input.strip() == "start"):
        start_server(config,log)
    elif( input.strip() == "stop"):
        stop_server(config,log)
    elif( input.strip() == "restart"):
        restart_server(config,log)
    if( input.strip() == "delete"):
        revert_install(config,log)

if __name__ == "__main__":
    main("tuxy.config")
