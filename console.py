#!/usr/bin/python3
"""
    module that handles the console
"""

import os
import re
import sys
import cmd
import json
from models.patient import Patient
from models.complaint import Complaint
from models.review import Review
from models.history import History
from class_find import classFind
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, tabulate
from models import storage
from prettytable import PrettyTable
from models.utils import Utils
from termcolor import colored

class ReportManager(cmd.Cmd):
    """
        command line interpreter
    """


    prompt = "\033[92m🚀 > \033[0m"
    report = ""


    def preloop(self):
        print()
        Utils.print_center(colored("Welcome to Clerking_Report_Generator".center(30, '×'), "black", "on_red"))
        column = ['Commands', "Usage"]
        commands = ['create', 'find', 'show', 'destroy', 'report', 'update', 'all', 'count', 'quit']
        myTab = PrettyTable()

        # Add Columns
        myTab.add_column(column[0], [index for index in commands])
        myTab.add_column(column[1], [f"help {index}"  for index in commands])
        
        print(myTab)
        print("All classes are dependent on the Patient class")


    def postloop(self):
        print()
        Utils.print_center(colored("Bye!!".center(30, '-'), "black", "on_red"))
        print()

    def do_quit(self, line):
        """
            Quit command to exit the program
            Alternative methods to quit the program:
                => type "quit" and press enter
                => Ctrl + D
                => Ctrl + C
        """
        return True

    def do_EOF(self, line):
        """
            Exit
        """
        return True

    def emptyline(self):
        """
            handles empty line
            action: prints a new line
        """
        pass

    def do_checkLine(self, line):
        """
            checkLine handles parameter check
            completeness for each command
        """
        if not line:
            print("** class name missing **")
            return False
        else:
            arg_list = cmd.Cmd.parseline(self, line)
            if arg_list[0] not in classFind():
                print("** class doesn't exist **")
                return False
            elif len(arg_list[2].split()) <= 2:
                print("** instance id missing **")
                return False
            else:
                flag = (arg_list[2].split())[-1]
                instance_key = arg_list[0] + "." + arg_list[1].split()[0]
                all_objs = storage.all()
                if int(flag) > 1:
                    return True
                if instance_key not in all_objs:
                    print("** no instance found **")
                    return False
                if int(flag) and len(arg_list[2].split()) == 3:
                    print("** attribute name missing **")
                    return False
                if int(flag) and len(arg_list[2].split()) == 4:
                    print("** value missing **")
                    return False
        return True

    def do_create(self, class_name):
        """
            creates a new instance of a class
            Usage:  create <class_name> => Patient
                    <class_name>.create()
                    create Patient
            action: creates an object and prints its allocated id
                    saves to a file
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in classFind():
            print("** class doesn't exist **")
        else:
            # Get the class from the global namespace
            my_class = globals()[class_name]
            # Instantiate an object from the class
            instance = my_class()
            storage.new(instance)
            storage.save()
            print(instance.id)

    def do_show(self, line):
        """
            shows the attributes an instance of a class
            Usage: show <class_name> <instance.id>
                   <class_name>.show("<instance.id>")
                   Example: show Patient 546-894-904-479
                            Patient.show(546-894-904-479)
            action: prints instance.__dict__
        """
        nline = line + ' 0'
        if cmd.Cmd.onecmd(self, f"checkLine {nline}"):
            arg_list = cmd.Cmd.parseline(self, line)
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                try:
                    if obj['id'] == arg_list[1] or obj['patient_id'] == arg_list[1]:
                        my_class = globals()[arg_list[0]]
                        instance = my_class(**obj)
                        instance.to_table()
                        int_dict = instance.to_dict()
                        for data in int_dict.keys():
                            if isinstance(int_dict[data], dict):
                                Utils.print_center("----------------------------------")
                                Utils.print_center(f"{data.capitalize()}\n")
                                print(tabulate(int_dict[data]))
                except(AttributeError, KeyError):
                    continue


    def do_destroy(self, line):
        """
            destroys an instance of a class
            Usage: destroy <class_name> <instance.id>
                   <class_name>.destroy("<instance.id>")
                   Example: destroy Patient 546-894-904-479
                            Patient.destroy(546-894-904-479)
            action: prints instance.__dict__
                    saves changes to file
        """
        nline = line + ' 0'
        if cmd.Cmd.onecmd(self, f"checkLine {nline}"):
            arg_list = cmd.Cmd.parseline(self, line)
            all_objs = storage.all()
            for obj_id in all_objs.copy().keys():
                obj = all_objs[obj_id]
                if obj['id'] == arg_list[1]:
                    del (all_objs[obj_id])
                else:
                    try:
                        if obj['patient_id'] == arg_list[1]:
                            del (all_objs[obj_id])
                    except (AttributeError, KeyError):
                        pass
            storage.save()
            print(f"{line} destroyed successfully!")


    def do_all(self, line):
        """
            prints all the instances of a class
            Usage: all
                   all <class_name>
                   <class_name>.all()
            action: prints all instance.__dict__ of a clsss from JSON file
        """
        arg_list = cmd.Cmd.parseline(self, line)
        if arg_list[0] is not None and arg_list[0] not in classFind():
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            all_objs_list = []
            for obj_id in all_objs.copy().keys():
                obj = all_objs[obj_id]
                if obj["__class__"] == arg_list[0] or arg_list[0] is None:
                    all_objs_list.append(obj)
            print(all_objs_list)

    def do_update(self, line):
        """
            updates an instance of a class
            Usage: update <cls_name> <instance.id> <attr> <value>
                   <cls_name>.update("<instance.id>", "<attr>", "<value>")
            Example: update Patient 546-894-904-479 family_number +123456789
            action: changes value in instance.__dict__[key]
            if key matches attr
                    creates value in instance.__dict__[key]
            if key is not in dict
                    saves changes to file
        """
        nline = line + ' 1'
        if cmd.Cmd.onecmd(self, f"checkLine {nline}"):
            arg_list = cmd.Cmd.parseline(self, line)
            all_objs = storage.all()
            for obj_id in all_objs.copy().keys():
                obj = all_objs[obj_id]
                if obj['id'] == arg_list[1].split()[0]:
                    if arg_list[1].split()[1] not in obj:
                        obj[arg_list[1].split()[1]] = \
                        arg_list[1].split()[2].replace('"', '')
                    else:
                        for key, value in obj.items():
                            if key == arg_list[1].split()[1]:
                                obj[key] = arg_list[1].\
                                    split()[2].replace('"', '')
                    storage.save()

    def default(self, line):
        """
            handles:
                    <class name>.update()
                    <cls_name>.<cmd>("<instance.id>", "<attr>", "<value>")
                    <class name>.update(<id>, <dictionary representation>)
                    unknown commands
        """
        flag = 0
        if re.match(
                r'[a-zA-Z]+\.{1}[a-zA-Z]+\({1}.*\){1}', line)\
                or re.match(
                        r'[a-zA-Z]+\.{1}[a-zA-Z]+\("[-\w]+", .*\)', line):
            if "{" in line and "}" in line:
                flag = 1
            arg_list = [item for item in re.split(r'[("\',: {}.)]', line) if item]
            if f"do_{arg_list[1]}" in ReportManager.__dict__:
                if len(arg_list) == 2:
                    return cmd.Cmd.onecmd(self, f"{arg_list[1]} {arg_list[0]}")
                else:
                    string = arg_list[1] + f" {arg_list[0]} {arg_list[2]} "
                    count = 0
                    for i in range(len(arg_list)):
                        if i > 2:
                            string += f" {arg_list[i]} "
                            count += 1
                        if count == 2 or (not flag and i == len(arg_list) - 1):
                            count = 0
                            cmd.Cmd.onecmd(self, string)
                            string = arg_list[1] +\
                                f" {arg_list[0]} {arg_list[2]} "
            else:
                return cmd.Cmd.default(self, f"{arg_list[1]}")
        else:
            return cmd.Cmd.default(self, line)

    def do_count(self, line):
        """
            counts all the instances of a class and prints the number
            Usage:  
                    count <class_name>
                    <class_name>.count()
            Example: 
                     count Patient
                     Patient.count()
            action: counts the number of objects of type <class_name>
                    in json file and prints on the screen
        """
        arg_list = cmd.Cmd.parseline(self, line)
        if arg_list[0] is not None and arg_list[0] not in classFind():
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            all_objs_list = []
            for obj_id in all_objs.copy().keys():
                obj = all_objs[obj_id]
                if obj["__class__"] == arg_list[0]:
                    all_objs_list.append(obj)
            print(len(all_objs_list))

    def do_find(self, line):
        """
            finds the instance_id of a class
            Usage: 
                    find <cls_name> <first_name>
                    find <cls_name> <first_name> <second_name>
            Example: 
                    find Patient Andrew
                    find Patient Andrew Tate
            action: checks all the saved objects and returns
                    the id of <first_name> if exists
        """
        nline = line + ' 2'
        flag = 0
        if cmd.Cmd.onecmd(self, f"checkLine {nline}"):
            arg_list = cmd.Cmd.parseline(self, line)
            all_objs = storage.all()
            for obj_id in all_objs.copy().keys():
                obj = all_objs[obj_id]
                ag_list = arg_list[1].split()
                if len(ag_list) == 1:
                    if obj['__class__'] == 'Patient':
                        try:
                            for data in obj['biodata']:
                                if isinstance(obj['biodata'][data], str) and\
                                    ag_list[0].lower() == obj['biodata'][data].lower():
                                    # this is obsolete since it prints a table
                                    # pat = obj['biodata']
                                    # print(f"The id for {pat['first_name']} {pat['last_name']} is {obj['id']}")
                                    print(tabulate(obj))
                                    flag = 1
                        except KeyError:
                            pass
                elif len(ag_list) > 1:
                    ...
            if not flag:
                print("This patient either does not exist or has no biodata filled")
                ans = Utils.safeInput("Will you like to create a new Patient? Y/N => ")
                while ans.lower() not in ['y', 'n']:
                    ans = input("Type Y/N for the above question")
                if ans.lower() == "y":
                    cmd.Cmd.onecmd(self, "create Patient")
                else:
                    print("find operation completed. Patient does not exist!")


    def do_save(self, line):
        """
            saves a Patient's report in a file
            Usage: save <class_name> <instance.id>
                   <class_name>.save("<instance.id>")
        """
        path = "reports"
        file_path = line.split()[0] + '_' + line.split()[1]
    
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:

            # Create a new directory because it does not exist
            os.makedirs(path)
            print("A new directory is created!")
        os.chdir(path)
        
        with open(file_path, "w+", encoding="utf-8") as file:
            file.write(ReportManager.report)
        os.chdir('..')
    
    
    def do_report(self, line):
        """
            generate a comprehensive report for a Patient's class
            Usage: report <class_name> <instance.id>
                   <class_name>.save("<instance.id>")
            action:
                    compiles a report using Patients data stored with
                    <id> and saves changes to file
        """
        nline = line + ' 0'
        if cmd.Cmd.onecmd(self, f"checkLine {nline}"):
            arg_list = cmd.Cmd.parseline(self, line)
            all_objs = storage.all()
            biodata = []
            for obj_id in all_objs.copy().keys():
                obj = all_objs[obj_id]
                if obj['id'] == arg_list[1]:
                    patient_data = all_objs[obj_id]
                    biodata = patient_data['biodata']

                    if biodata['first_name'] and biodata['last_name']:
                        name_initials = biodata['first_name'][0].upper() + '.' + biodata['last_name'][0].upper()
                    age = biodata['age']
                    if biodata['sex']:
                        
                        sex = "female" if biodata['sex'][0].lower() == "f" else "male"

                    pronoun = "she" if sex == "female" else "he"
                    occupation = biodata['occupation'].lower()
                    marital_status = biodata['marital_status'].lower()
                    if pronoun == "she":
                        title = "Mrs" if marital_status == "married" else "Miss"
                    else:
                        title = "Mr"
                    address = biodata['address'].lower()
                    religion = biodata['religion'].lower()
                    tribe = biodata['tribe'].lower()
                    educational_level = biodata['educational_level'].lower()

                    ReportManager.report += f"      I am presenting {title} {name_initials}, a {age}-year-old {occupation} who resides at {address}. {pronoun} is {tribe} and a {religion} with {educational_level} level of education."

                else:
                    try:
                        if obj['patient_id'] == arg_list[1]:
                            if obj['__class__'] == 'Complaint':
                                complaint = obj['complaint']
                                file_path = biodata['first_name'] + ' ' + obj['patient_id']

                                com_list = list(complaint.keys())
                                for com in com_list:
                                    ReportManager.report += f"\n    {pronoun.capitalize()} presented with {com} of {complaint[com]} duration, "
                                ReportManager.report += "and was admitted via the accident and emergency ward.\n\t\033[92m History of Presenting Complaints \033[0m\n"
                                history = obj['history_of_complaint']
                                hist_list = list(history.keys())
                                for his in hist_list:
                                    ReportManager.report += f"{his}: {history[his]}\n" if history[his] != '' else f"no {his}, "
                            elif obj['__class__'] == 'History':
                                ReportManager.report += "\n\t\033[92m History Analysis \033[0m\n"
                                for history in obj:
                                    if isinstance(obj[history], dict):
                                        history_dict = obj[history]
                                        hist_list = list(history_dict.keys())
                                        for his in hist_list:
                                            ReportManager.report += f"{his}: {history_dict[his]}\n" if history_dict[his] != '' else f"no {his}, "
                                cmd.Cmd.onecmd(self, f"save {file_path}")
                                print("Report Compilation Complete..")
                    except (AttributeError, KeyError):
                        continue


if __name__ == '__main__':
    try:
        ReportManager().cmdloop()
    except KeyboardInterrupt:
        print("Exiting....")
        sys.exit()
