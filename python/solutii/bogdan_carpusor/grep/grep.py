#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Docstring
"""
from __future__ import print_function
import os
import config


class Grep(object):
    """
    Clasa principala ce evalueaza comenzile
    si cauta in fisiere
    """
    def __init__(self, options):
        self.file_list = []
        self.pattern = options[2]
        self.to_replace = ""
        self.counter = 0
        self.word_dict = {}

        if "t" in options[1]:
            self.file_list = options[2:]
        else:
            if "r" in options[1]:
                if "s" in options[1]:
                    self.to_replace = options[3]
                    Grep.get_file_list(options[4], self.file_list)
                else:
                    Grep.get_file_list(options[3], self.file_list)
            else:
                if "s" in options[1]:
                    self.to_replace = options[3]
                    self.file_list = options[4:]
                else:
                    self.file_list = options[3:]

    @staticmethod
    def evaluate_input(args):
        """
        Metoda evalueaza corectitudinea datelor
         de intrare
        """
        argument_length = len(args)
        if argument_length < 3:
            print("Invalid input --- Useage example:")
            return False
        elif "-" not in args[1]:
            print("Invalid options --- Useage example:")
            return False
        elif "i" in args[1] and "e" in args[1]:
            print("Invalid options --- Useage example:")
            return False
        elif "s" in args[1] and argument_length < 5:
            print("Missing Parameter --- Useage example:")
            return False
        else:
            return True

    @staticmethod
    def get_file_list(folder_path, file_list):
        """
        Functia recurenta aduna toate fisierele
        dintr-un folder intr-o lista
        """
        folder_list = os.listdir(folder_path)
        for item in folder_list:
            new_path = os.path.join(folder_path, item)
            if item in config.IGNORE_FILES:
                continue
            elif os.path.isfile(new_path):
                file_list.append(new_path)
                print(file_list)
            elif os.path.isdir(new_path):
                Grep.get_file_list(new_path, file_list)

    @staticmethod
    def process_options(options):
        """
        Functia evalueaza optiunile de prelucrare
         returnand o lista
        """
        if 'i' in options:
            method = 'i'
        elif 'e' in options:
            method = 'e'
        elif 't' in options:
            method = 't'
        else:
            return False
        color = False
        replace = False
        count = False
        if "n" in options:
            count = True
        if "s" in options:
            replace = True
        if "c" in options:
            color = True
        return [replace, count, color, method]

    def process_string(self, line, replace, count, color):
        """
        Metoda prelucreaza o line in cazul in care sunt
        cautate orice fel de aparitii (-i)
        """
        if count:
            self.counter += line.count(self.pattern)
        temp_list = []
        line = line.split(self.pattern)
        pattern = self.pattern
        if replace:
            pattern = self.to_replace
        for value in line[:-1]:
            if color:
                pattern = "".join([config.RED, pattern, config.END])
                temp_value = "".join([value, pattern])
            else:
                pattern = "".join([config.BOLD, pattern, config.END])
                temp_value = "".join([value, pattern])
            temp_list.append(temp_value)
        temp_list.append(line[-1])
        return "".join(temp_list)

    def process_list(self, line, replace, count, color):
        """
        Functia prelucreaza o linie in cazul in care
         cautarea trebuie sa fie exacta (-e)
        """
        if count:
            self.counter += line.count(self.pattern)
        temp_list = []
        flag = False
        for word in line:
            if word == self.pattern:
                flag = True
                if replace:
                    word = self.to_replace
                if color:
                    word = "".join([config.RED, word, config.END])
                else:
                    word = "".join([config.BOLD, word, config.END])
            temp_list.append("".join([word, " "]))
        if flag:
            return "".join(temp_list)
        else:
            return False

    def update_dict(self, line):
        """
        Functia adauga sau incrementeaza numarul de aparitii
         al unui cuvant intr-un fisier
        """
        word_list = line.split(" ")
        for word in word_list:
            if word.isalnum():
                self.word_dict[word] = self.word_dict.setdefault(word, 0) + 1

    def process_file(self, options):
        """
        Functia citeste fiecare linie din fisier
         prelucrand in functie de optiunile de intrare
        """
        options = Grep.process_options(options)
        for file_name in self.file_list:
            with open(file_name, 'r+') as file_obj:
                line_no = 0
                for line in file_obj:
                    line_no += 1
                    if options[3] == "i":
                        temp_line = line.lower()
                        self.pattern.lower()
                        if self.pattern in line:
                            line = self.process_string(
                                temp_line, options[0], options[1], options[2])
                            print("File {0}: Line {1}: {2}"
                                  .format(file_obj.name, line_no, line))
                    elif options[3] == "e":
                        temp_line = line.split(" ")
                        if self.pattern in line:
                            line = self.process_list(
                                temp_line, options[0], options[1], options[2])
                            if line:
                                print("File {0}: Line {1}: {2}"
                                      .format(file_obj.name, line_no, line))
                    elif options[3] == "t":
                        self.update_dict(line)
            if options[3] == "t":
                print([key for key, value in self.word_dict.iteritems()
                       if value in sorted(self.word_dict.values())[-5:]])
