#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy nu dorește să uite de nici un eveniment important pentru el
sau pentru cineva apropiat lui așa că își dorește un sistem care
să îi permită gestiunea acestor evenimente.

Script-ul `executor` va primi o sarcină generată / pregătită de
către script-ul `scheduler` și va încerca să îndeplinească toate
cerințele ce sunt încapsulate în aceasta.
"""
from __future__ import print_function
from task import TaskManager


def executor():
    """Procesează informațile din cadrul unei sarcini și încearcă
    să le îndeplinească.
    """
    task_manager = TaskManager()
    task_manager.map_tasks()
    task_manager.task_list[0].initialize_task()
    task_manager.task_list[0].execute_task()
    task_manager.delete_task(0)
    task_manager.persist_tasks()

if __name__ == "__main__":
    executor()
