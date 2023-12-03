#!/usr/bin/python3
"""
    amenity module
"""

from models.base_model import BaseModel
from models.utils import Utils
from colorama import init
from termcolor import colored

init()
class History(BaseModel):
    """
        Amenity class for all User object
    """

    name = ""
    ph = {}
    dh = {}
    sh = {}
    ih = {}
    fh = {}

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
        print(colored("Getting details of Patient's history...", "green"))
        self.prev_history()
        self.drug_history()
        self.immunization_history()
        self.family_history()
        self.social_history()
        self.save()


    def prev_history(self):
        Utils.print_center(colored("Previous History", 'green'))
        ph = [
                'Previous_illnesses_Operations_or_Accidents', 'Diabetes', 'Rheumatic_fever', 'Diphtheria', 'Bleeding_tendencies', 'Asthma', 'Hay_fever', 'Allergies', 'Tuberculosis', 'Sexually_transmitted_diseases', 'Tropical_diseases', 'Hypertension', 'Diabetes', 'Blood_Transfusion'
                ]

        print(colored("\nAnswer Yes/No for all the following questions, if your response is No, press ENTER\n", "red"))

        for history in ph:
            h = input(f"Does the Px have a previous history of [{colored(history, 'blue')}] => ")
            if h != '':
                History.ph[history] = input(f"Enter in details the history of this illness if present [{colored(history, 'blue')}] => ")

        self.prev_history = History.ph


    def drug_history(self):
        Utils.print_center(colored("Drug History", 'green'))
        dh = [
                'Insulin', 'Steroids', 'Antidepressants', 'contraceptives', 'Drug_abuse', 'Traditional'
                ]
        print(colored("\nAnswer Yes/No for all the following questions, if your response is No, press ENTER\n", "red"))
        for drug in dh:
            h = input(f"Has the patient used [{colored(drug, 'blue')}] in the past? => ")
            if h != '':
                History.dh[drug] = input(f"Enter the name of the drug or unascertained if used [{colored(drug, 'blue')}] => ")
        self.drug_history = History.dh


    def immunization_history(self):
        Utils.print_center(colored("Immunization History", 'green'))
        ih = ['BCG', 'Diphtheria', 'Tetanus', 'COVID', 'Typhoid', 'Whooping_cough', 'Measles']
        print(colored("\nAnswer Yes/No for all the following questions, if your response is No, press ENTER\n", "red"))
        for history in ih:
            h = input(f"Does the patient have a previous history of [{colored(history, 'blue')}] immunization? => ")
            if h != '':
                History.ih[history] = input(f"Enter in details the history of this parameter [{colored(history, 'blue')}] => ")
        self.immunization_history = History.ih


    def family_history(self):
        Utils.print_center(colored("Family History", 'green'))
        fh = ['Causes_of_death_of_close_relatives', 'Familial_illnesses_in_siblings_and_offspring']
        print(colored("\nAnswer Yes/No for all the following questions, if your response is No, press ENTER\n", "red"))
        for history in fh:
            h = input(f"Does the patient have a family history of [{colored(history, 'blue')}] => ")
            if h != '':
                History.fh[history] = input(f"Enter in details the history of this parameter [{colored(history, 'blue')}] => ")
        self.family_history = History.fh


    def social_history(self):
        Utils.print_center(colored("Social History", 'green'))
        sh = [
                'Marital_status', 'Sexual_habits', 'Living_accommodation', 'Occupation', 'Exposure_to_industrial_hazards', 'Travel_abroad', 'Leisure_activities', 'Smoking_in pack_year', 'Drinking', 'Number_of_cigarettes_smoked_per_day', 'Units_of_alcohol_drunk_per_week', 'pap_smear']

        print(colored("\nAnswer Yes/No for all the following questions, if your response is No, press ENTER\n", "red"))
        for history in sh:
            h = input(f"Is the social history parameter [{colored(history, 'blue')}] relevant for this patient? => ")
            if h != '':
                History.sh[history] = input(f"Enter in details the history of this parameter [{colored(history, 'blue')}] => ")
        self.social_history = History.sh
