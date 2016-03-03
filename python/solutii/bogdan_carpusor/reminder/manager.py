#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy nu dorește să uite de nici un eveniment important pentru el
sau pentru cineva apropiat lui așa că își dorește un sistem care
să îi permită gestiunea acestor evenimente.

Script-ul `manager` îi oferă lui Tuxy posibilitatea de a adăuga
modifica sau șterge un eveniment.
"""
from __future__ import print_function
from copy import deepcopy
from task import TaskManager

OPTIONS = ['list', 'edit', 'delete', 'add']
TASK_TYPES = ['email', 'sms', 'pigeon', 'drone']

TASK_TEMPLATES = {
    'email': {
        'type': 'email',
        'content': '',
        'destination': '',
        'subject': '',
        'deadline': ''
    },
    'pigeon': {
        'type': 'pigeon',
        'deadline': '',
        'destination': '',
        'paper_type': '',
        'content': ''
    },
    'sms': {
        'type': 'sms',
        'deadline': '',
        'destination': '',
        'sender': '',
        'content': ''
    },
    'drone': {
        'type': 'drone',
        'deadline': '',
        'destination': '',
        'subject': '',
        'content': ''
    }
}


def list_options():
    """Functia afiseaza optiunile din
    meniul principal
    """

    print("Task Manager:")
    print("\t 1 - List current tasks")
    print("\t 2 - Add new task")
    print("\t 3 - Edit task")
    print("\t 4 - Delete task")
    print("\t 0 - Exit")


def get_input(option_type):
    """
    Functia parseaza inputul introdus
     de user
    """
    if option_type == "add":
        flag = False
        task_type = ""
        while not flag:
            task_type = raw_input("Task type: ")
            if task_type in TASK_TYPES:
                flag = True
            else:
                print("Invalid task name")
                print("Options: {0}".format(TASK_TYPES))
        task = deepcopy(TASK_TEMPLATES[task_type])
        for key in task.iteritems():
            if key != 'type':
                input_value = raw_input("%s: " % key)
                task[key] = input_value

        return task
    elif option_type == "get_id":
        task_id = raw_input("Insert task id: ")
        return task_id
    elif option_type == 'edit':
        pass


def manager():
    """Aplicație ce permite gestiunea evenimentelor."""
    task_manager = TaskManager()
    task_manager.map_tasks()

    flag = True
    while flag:
        list_options()
        option = raw_input("Insert option: ")
        if option == "1":
            print("Task list:")
            task_manager.list_tasks()
        elif option == "2":
            print("Adding new task:")
            task = task_manager.add_task(
                get_input("add")
            )
            task_manager.task_list.append(task)
        elif option == "3":
            print("Editing Task")
            task_manager.edit_task(
                int(get_input("get_id"))-1
            )
        elif option == "4":
            print("Deleting task")
            task_manager.delete_task(
                int(get_input("get_id")) - 1
            )
        elif option == "0":
            flag = False
        else:
            print("Invalid input. Try Again")

    task_manager.persist_tasks()

if __name__ == "__main__":
    manager()
