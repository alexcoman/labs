#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy își dorește un sistem care să automatizeze instalării unui proiect
pe infrastructura din `TuxyLand`.

Acest proiect de automatizare va primi un fișier de configurare ce va
conține toate instrucțiunile necesare pentru pregătirea mediului ideal
în care va rula `TuxyApp`.

Un exemplu de fișier de configurare ar putea fi: tuxy.config din
directorul python/date_intrare.

Trebuie să dezvoltați o aplicație care să primească un fișier de
configurare și să rezolve toate sarcinile precizate în acesta.

La sfârșit va trebui să ofere un fișier build.log care să descrie
toate lucrurile care s-au întâmplat.
"""

from __future__ import print_function
import subprocess
import time
import urllib2
import logging
import os
import yaml


DEFAULT_KEYS = ['before_install', 'config',
                'install', 'after_install', 'install_failed']
COMMAND_DICT = {
    'reboot': 'reboot',
    'download': 'download_file',
    'hostname': 'create_hostname',
    'users': 'create_user',
    'write_files': 'write_files',
    'run_script': 'run_script',
    'delete': 'delete',
    'shutdown': 'shutdown'
}

TEST = True


class Command(object):
    """
    Command class - encapsulates all the commands
    known by the config app
    """
    def __init__(self, options):
        self.options = options

    USER_OPTIONS = {
        'expiredate': '-e',
        'full_name': '-c',
        'groups': '-G',
        'password': '-p',
        'primary-group': '-g'
    }

    def download_file(self):
        """
        The method downloads a file to
         a custom location
        """
        logging.info('Downloading file')
        path_list = self.options['destination'].split('/')
        file_name = path_list.pop()
        path_list.insert(0, '/')
        folder_path = os.path.join(*path_list)
        try:
            web_file = urllib2.urlopen(self.options['source'])
            if not os.path.exists(self.options['destination']):
                os.mkdir(folder_path)

            with open(os.path.join(folder_path, file_name), 'w+') \
                    as output_file:
                output_file.write(web_file.read())
            web_file.close()
            output_file.close()
        except urllib2.HTTPError:
            logging.warning("Error while downloading file %s",
                            self.options['source'])
            return False

    def create_hostname(self):
        """
        The method creates a new hostname for the system
        """
        logging.info('Creating hostname')
        subprocess.call(['hostname', self.options])

    def create_user(self):
        """
        The method iterates through a user dictionary
         and creates users based on the properties
        """
        for user_name, options in self.options.iteritems():
            logging.info('Adding new user')
            command_list = ['useradd']
            for key, value in options.iteritems():
                if key in Command.USER_OPTIONS:
                    command_list.append(
                        Command.USER_OPTIONS[key]
                    )
                    if key == 'groups':
                        value = value[0]
                    command_list.append(value)
                else:
                    logging.warning('Invalid option. Ignoring field.')
            command_list.append(user_name)
            subprocess.call(command_list)

    def write_files(self):
        """
        The method iterates through a dictionary of files
        and creates them at a custom path
        """
        logging.info('Writing Files:')
        for key, value in self.options.iteritems():
            logging.info('Writing file %s', key)
            file_path = os.path.join(value['path'], str(key))
            if not os.path.exists(file_path):
                try:
                    os.makedirs(value['path'])
                except OSError:
                    logging.warning('Error creating folder %s', file_path)
                    return False
            output_file = open(file_path, 'w+')
            output_file.write(
                value['content']
            )
            output_file.close()
            if value['encoding'] == 'gzip':
                subprocess.check_call(['gzip', file_path])
                file_path = "".join([file_path, '.gz'])
            os.chmod(file_path, int(value['permissions']))
        return True

    def run_script(self):
        """
        The method runs a script based on the parameters
         specified in the config file
        """
        iterator = 0
        logging.info('Running script')
        env_var = dict(os.environ)
        for key, value in self.options['env_variables'].iteritems():
            env_var = dict(env_var, key=value)

        while iterator < self.options['attempts']:
            process = subprocess.Popen(self.options['command'],
                                       shell=self.options['shell'],
                                       cwd=self.options['cwd'],
                                       env=env_var)
            process.wait()
            if process.returncode is None:
                logging.warning('Script failed to run')
                iterator += 1
            else:
                return True
            time.sleep(3)
        return False

    def delete(self):
        """
        The method deletes a specified file
        """
        logging.info('Deleting file %s', self.options['path'])
        if os.path.exists(self.options['path']):
            command_list = ['rm']
            if os.path.isdir:
                command_list.append('-r')
            if self.options['method'] == "force":
                command_list.append('-f')
            command_list.append(self.options['path'])
            subprocess.call(command_list)
            return True
        else:
            logging.warning("Invalid path: %s", self.options['path'])
            return False

    def reboot_command(self):
        """
        The method sends a command to reboot
         the system
        """
        logging.info('Rebooting system')
        command_list = ['reboot']
        if self.options['method'] == 'force':
            command_list.append('-f')
        if not TEST:
            subprocess.call(command_list)

    def shutdown(self):
        """
        The method send a command to shutdown
        the system
        """
        logging.info('Running shutdown')
        command_list = ['shutdown']
        if self.options['method'] == 'hard':
            command_list.append('-H')
        else:
            command_list.append('-h')

        command_list.append('now')
        if not TEST:
            subprocess.call(command_list)


def run_commands(commands):
    """
    The function evaluates the yaml
     file and executes specifi commands
    """
    logging.info("Running command list.")
    if isinstance(commands, list):
        for command in commands:
            for key, value in command.iteritems():
                if key in COMMAND_DICT.keys():
                    exec_command = Command(value)
                    exec_method = getattr(exec_command, COMMAND_DICT[key])
                    exec_method()
                else:
                    logging.warning('Command is not'
                                    ' in the command list. Skipping line')
    elif isinstance(commands, dict):
        for key, value in commands.iteritems():
            if key in COMMAND_DICT.keys():
                exec_command = Command(value)
                exec_method = \
                    getattr(exec_command, COMMAND_DICT[key])
                exec_method()
            else:
                logging.warning('Command is not'
                                ' in the command list. Skipping line')
    else:
        return False


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return

    logging.basicConfig(filename='build.log',
                        level=logging.DEBUG,
                        format='%(levelname)s %(asctime)s %(message)s')
    logging.info('Running instalation configs')
    run_commands(config['before_install'])
    run_commands(config['config'])
    if run_commands(config['install']):
        logging.info('Installation finished successful')
        run_commands(config['after_install'])
    else:
        logging.info('Instalation incomplete')
        run_commands(config['install_failed'])

if __name__ == "__main__":
    main("../../../date_intrare/tuxy.config")
