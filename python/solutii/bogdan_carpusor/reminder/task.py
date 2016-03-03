#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Scriptul task.py defineste modul de
salvare a task-urilor ce vor fi ordonate
 de scheduler
"""
from __future__ import print_function
import json


class SendTask(object):
    """
    Clasa generala pentru un task
    """
    def __init__(self, time, recurrence, destination, content, task_id):
        self.deadline = time
        self.recurrence = recurrence
        self.destination = destination
        self.content = content
        self.task_id = int(task_id)

    def initialize_task(self):
        """
        Functie pentru partea de executare
        """
        print("loading task number %s..." % self.task_id)

    def to_dict(self):
        """
        Functia transforma o instanta
        intr-un dictionar
        """
        task_dict = {self.task_id: {
            'content': self.content,
            'destination': self.destination,
            'deadline': self.deadline
        }}
        return task_dict

    def print_task(self):
        """
        Functia printeaza formatat
        o instanta a unui task
        """
        print('{0} -------------'.format(self.task_id))
        print('\t Deadline -- {0}'.format(self.deadline))
        print('\t To: {0}'.format(self.destination))
        print('\t Content: {0}'.format(self.content))

    def execute_task(self):
        """
        Functie pentru partea de executare
        """
        print('Executing task {0}'.format(self.task_id))


class EmailTask(SendTask):
    """
    Clasa pentru un anumit tip de task
    """
    def __init__(self, recurrence, args):
        SendTask.__init__(self, args['deadline'], recurrence,
                          args['destination'], args['content'], args['id'])
        self.subject = args['subject']

    def send_email(self):
        """
        Functie pentru partea de executare
        """
        print("sending email to %s" % self.destination)

    def to_dict(self):
        """
        Functia transforma un obiect
        intr-un dictionar
        """
        task_dict = SendTask.to_dict(self)
        task_dict[self.task_id].update({'type': 'email'})
        task_dict[self.task_id].update({'subject': self.subject})
        return task_dict

    def print_task(self):
        """
        Functia afiseaza formatat un task
        """
        SendTask.print_task(self)
        print('\t Subject: {0}'.format(self.subject))
        print('---------------- {0}\n'.format(type(self).__name__))

    def execute_task(self):
        """
        Functie pentru partea de executare
        """
        SendTask.execute_task(self)
        self.send_email()


class PigeonTask(SendTask):
    """
    Clasa pentru un anumit tip de task
    """
    def __init__(self, recurrence, args):
        SendTask.__init__(self, args['deadline'], recurrence,
                          args['destination'], args['content'], args['id'])
        self.paper_type = args['paper_type']

    def send_message(self):
        """
        Functie pentru partea de executare
        """
        print("sending message to %s" % self.destination)

    def choosing_pigeon(self):
        """
        Functie pentru partea de executare
        """
        print("choosing proper pigeons to carry the "
              "following paper format: %s" % self.paper_type)

    def to_dict(self):
        """
        Functia transforma un obiect
        intr-un dictionar
        """
        task_dict = SendTask.to_dict(self)
        task_dict[self.task_id].update({'type': 'pigeon'})
        task_dict[self.task_id].update({'paper_type': self.paper_type})
        return task_dict

    def print_task(self):
        """
        Functia afiseaza formatat un task
        """
        SendTask.print_task(self)
        print('\t Paper Type: {0}'.format(self.paper_type))
        print('---------------- {0}\n'.format(type(self).__name__))

    def execute_task(self):
        """
        Functie pentru partea de executare
        """
        SendTask.execute_task(self)
        self.choosing_pigeon()
        self.send_message()


class SmsTask(SendTask):
    """
    Clasa pentru un anumit tip de task
    """
    def __init__(self, recurrence, args):
        SendTask.__init__(self, args['deadline'], recurrence,
                          args['destination'], args['content'], args['id'])
        self.sender = args['sender']

    def send_sms(self):
        """
        Functie pentru partea de executare
        """
        print("Sending sms to %s" % self.destination)

    def to_dict(self):
        """
        Functia transforma un obiect
        intr-un dictionar
        """
        task_dict = SendTask.to_dict(self)
        task_dict[self.task_id].update({'type': 'sms'})
        task_dict[self.task_id].update({'sender': self.sender})
        return task_dict

    def print_task(self):
        """
        Functia afiseaza formatat un task
        """
        SendTask.print_task(self)
        print('\t Sender: {0}'.format(self.sender))
        print('---------------- {0}\n'.format(type(self).__name__))

    def execute_task(self):
        """
        Functie pentru partea de executare
        """
        SendTask.execute_task(self)
        self.send_sms()


class DroneTask(SendTask):
    """
    Clasa pentru un anumit tip de task
    """
    def __init__(self, recurrence, args):
        SendTask.__init__(self, args['deadline'], recurrence,
                          args['destination'], args['content'], args['id'])
        self.sender = args['sender']

    def send_drone(self):
        """
        Functie pentru partea de executare
        """
        print("Initializing drone...")
        print("Computing route for %s..." % self.destination)
        print("Bye bye")

    def to_dict(self):
        """
        Functia transforma un obiect
        intr-un dictionar
        """
        task_dict = SendTask.to_dict(self)
        task_dict[self.task_id].update({'type': 'drone'})
        task_dict[self.task_id].update({'sender': self.sender})
        return task_dict

    def print_task(self):
        """
        Functia afiseaza formatat un task
        """
        SendTask.print_task(self)
        print('\t Sender: {0}'.format(self.sender))
        print('---------------- {0} \n'.format(type(self).__name__))

    def execute_task(self):
        """
        Functie pentru partea de executare
        """
        SendTask.execute_task(self)
        self.send_drone()


class TaskFactory(object):
    """
    Fabrica pentru crearea taskurilor
    """
    @staticmethod
    def create_task(dict_args, recurrence=False):
        """
        Functia instantiaza un task
        in functie de tipul acestuia
        """
        if dict_args['type'] == "email":
            return EmailTask(recurrence, dict_args)
        elif dict_args['type'] == "pigeon":
            return PigeonTask(recurrence, dict_args)
        elif dict_args['type'] == "sms":
            return SmsTask(recurrence, dict_args)
        elif dict_args['type'] == "drone":
            return DroneTask(recurrence, dict_args)
        else:
            return False


class TaskManager(object):
    """
    Clasa care serverste ca principala
    interfata cu taskurile
    """
    TASKS_FILE_PATH = "tasks.json"

    def __init__(self):
        self.task_list = []

    def map_tasks(self):
        """
        Functia citeste un fisier json
        si creaza o lista de taskuri
        """
        input_file = open(self.TASKS_FILE_PATH, 'r')
        json_tasks = json.load(input_file)
        for task_id in json_tasks:
            task_dict = {'id': task_id}
            for key in json_tasks[task_id]:
                task_dict.update({key: json_tasks[task_id][key]})
            self.task_list.append(TaskFactory.create_task(task_dict))

    def persist_tasks(self):
        """
        Functia scrie in fisierul json
        taskurile dupa modificarile facute
        asupra lor
        """
        task_dict = {}
        for task in self.task_list:
            task_dict.update(task.to_dict())

        with open('tasks.json', 'w+') as output_file:
            json.dump(task_dict, output_file)

    def add_task(self, task):
        """
        Functia adauga un nou task in lista
        """
        task.update({'id': len(self.task_list)+1})
        return TaskFactory.create_task(
            task
        )

    def edit_task(self, task_id):
        """
        Functia editeaza unul din taskurile
        existente
        """
        task = self.task_list[task_id]
        print("Insert new value press enter:")
        deadline = raw_input("New deadline: ")
        if deadline:
            task.deadline = deadline
        destination = raw_input("New destination: ")
        if destination:
            task.destination = destination
        if type(task).__name__ == 'EmailTask':
            argument = raw_input("New subject: ")
            if argument:
                task.subject = argument
        elif type(task).__name__ == "PigeonTask":
            argument = raw_input("New paper type: ")
            if argument:
                task.paper_type = argument
        elif type(task).__name__ in ["DroneTask", "SmsTask"]:
            argument = raw_input("New sender: ")
            if argument:
                task.sender = argument
        content = raw_input("New content: ")
        if content:
            task.content = content

    def delete_task(self, task_id):
        """Functia sterge un task
        si updateaza id-urile taskurilor existente
        """
        self.task_list.pop(task_id)
        self.update_id()

    def update_id(self):
        """Functia reface id-urile
        taskurilor din lista
        """
        task_id = 0
        for task in self.task_list:
            task.id = task_id
            task_id += 1

    def list_tasks(self):
        """
        Functia afiseaza toate task-urile
        din lista
        """
        if len(self.task_list) == 0:
            print("You have no more tasks!")
        else:
            for task in self.task_list:
                task.print_task()
