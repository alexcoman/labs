#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy nu dorește să uite de nici un eveniment important pentru el
sau pentru cineva apropiat lui așa că își dorește un sistem care
să îi permită gestiunea acestor evenimente.

Script-ul `scheduler.py` se va ocupa cu planificarea unei acțiuni
ce trebuie să fie executată de script-ul `executor.py`.

Un exemplu de acțiune ar putea fi:

29-03-2016-send-email
---
To: uxy@pinguinescu.ro
Subject: La mulți ani!
Content: Fie ca ...
"""
from __future__ import print_function
import time
from task import TaskManager


def list_options():
    """Functia afiseaza optiunile din
    meniul principal
    """
    print("Schedule Tasks:")
    print("\t 1 - By task deadline")
    print("\t 2 - By type")
    print("\t 3 - Manual")
    print("\t 0 - Exit")


def schedule_by_deadline(task_list):
    """
    Functia programeaza taskurile in
     functie de deadline
    """
    return sorted(task_list,
                  key=lambda task:
                  time.strptime(task.deadline, '%d %m %Y'))


def schedule_manually(task_list, task_order):
    """
    Functia programeaza taskurile
     in functie de inputul userului
    """
    new_list = []
    for value in task_order:
        new_list.append(task_list[int(value)])
    return new_list


def scheduler():
    """Planifică evenimentele."""
    task_manager = TaskManager()
    task_manager.map_tasks()
    print("Current task queue: ")
    task_manager.list_tasks()
    list_options()
    input_option = raw_input("Choose schedule type")
    if input_option == "1":
        task_manager.task_list = \
            schedule_by_deadline(task_manager.task_list)
    if input_option == "2":
        pass
    if input_option == "3":
        task_order = raw_input("Order tasks: ")
        task_manager.task_list = schedule_manually(
            task_manager.task_list, task_order.split(' '))
    task_manager.list_tasks()
    task_manager.update_id()
    task_manager.list_tasks()
    task_manager.persist_tasks()

if __name__ == "__main__":
    scheduler()
