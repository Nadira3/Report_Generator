#!/usr/bin/python3
"""
    user module
"""
from models.base_model import BaseModel
from models.complaint import Complaint
from models.review import Review
from models.history import History
from models.utils import Utils
from termcolor import colored
from prettytable import PrettyTable


class Patient(BaseModel):
    """
        User class for all other classes
    """

    biodata = {}

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.bio_data()
            pc = Complaint()
            pc.patient_id = self.id
            self.patient_id = pc.id
            pc.save()
            history = History()
            history.patient_id = self.id
            self.history_id = history.id
            history.save()
            review = Review()
            review.patient_id = self.id
            self.review_id = review.id
            review.save()
            self.save()
    

    def bio_data(self):
        """
            initialize the first and last name
        """

        patient_unit = ['medicine', 'surgery', 'obstetrics', 'gynaecology', 'paediatrics']
        column = ['Index', "Available_Units"]
        myTab = PrettyTable()

        # Add Columns
        myTab.add_column(column[0], [index for index in range(len(patient_unit))])
        myTab.add_column(column[1], patient_unit)
        
        print(colored("Getting Biodata... ", 'green'))

        biodata_dict = {
                'data': ['first_name', 'last_name', 'age', 'sex', 'occupation', 'marital_status', 'address', 'religion', 'tribe', 'educational_level', 'informant_name', 'informant_age'],
                'medicine': [],
                'surgery': [],
                'obstetrics': ['LMP', 'cycle_length', 'flow_length', 'parity', 'gravidity', 'EGA', 'EDD'],
                'gynaecology': ['LMP', 'cycle_length', 'flow_length'],
                'paediatrics': ['mode_of_delivery', 'developmental_milestones']
        }
        for data in biodata_dict['data']:
            Patient.biodata[data] = Utils.safeInput(f"[{colored(data, 'blue')}] => ")
        
        print()
        print(myTab)
        Utils.print_center(colored("If all patient's data have been taken, press ENTER => ".upper(), 'red'))
        Patient.biodata['unit'] = []
        while (unit := Utils.safeInput(colored("Enter the name of the patient's unit from the table for unique data entry => ", "green"))) != '':
            if unit.lower().strip() in biodata_dict:
                Patient.biodata['unit'].append(unit)
                data_list = biodata_dict[unit]
                for data in data_list:
                    Patient.biodata[data] = Utils.safeInput(f"[{colored(data, 'blue')}] => ")
            else:
                print(colored("Enter a valid unit. Make sure the spelling is correct! => ", 'black', 'on_red'))
        self.biodata = Patient.biodata
