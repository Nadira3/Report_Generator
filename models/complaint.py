#!/usr/bin/python3
"""
    place module
"""

from models.utils import Utils
from models.base_model import BaseModel
from colorama import init
from termcolor import colored
from prettytable import PrettyTable

init()

def xterize(symptom):
    result = {}
    character_dict = {
        'pain': ['site', 'onset', 'character', 'radiation', 'associated_symptoms', 'aggravating_factor', 'relieving_factor', 'timing', 'severity'],
        'swelling': ['site', 'size', 'shape', 'surface', 'surrounding_skin', 'base', 'edge', 'tenderness', 'neurovascular_component'],
        'vomit': ['volume', 'color', 'associated_symptoms', 'timing', 'nature', 'precipitant'],
        'bleeding': ['site', 'volume', 'color', 'associated_symptoms']
    }

    for parameter in character_dict[symptom]:
        result[parameter] = input(f"characterize the [{colored(symptom, 'blue')}] with [{colored(parameter, 'blue')}] => ")
    return result


class Complaint(BaseModel):
    """
        Place class for User object
    """
    pc = {}
    hpc = {}

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
        self.get_pc()
        self.pc_history()
        self.save()
    
    def get_pc(self):
        print(colored("Getting Presenting Complaints..... ", 'green'))
        while (symptom := input(f"[symptom] => ")) != "":
            Complaint.pc[symptom] = input("[duration] mins/secs/hrs/days/weeks/months/years => ")
        self.complaint = Complaint.pc


    def pc_history(self):
        print(colored("Getting History of Presenting Complaints..... ", 'green'))
        Utils.print_center(colored("        Pointer => History of the present complaint (HPC): Include the answers to the direct questions concerning the system of the presenting complaint\n", "red"))
        direct_questions = {
                'alimentary': ['Appetite', 'Diet', 'Weight', 'Nausea', 'Odynophagia', 'Dysphagia', 'Regurgitation', 'Flatulence', 'Heartburn', 'Vomiting', 'Haematemesis', 'Indigestion_pain', 'Abdominal_pain', 'Jaundice', 'Abdominal_distension', 'Bowel_habit', 'Nature_of_stool', 'Rectal_bleeding', 'Mucus', 'Slime', 'Prolapse', 'Incontinence', 'Tenesmus', 'Swelling', 'Weight_loss', 'Hemoptysis'],
                'respiratory': ['Cough', 'Sputum', 'Haemoptysis', 'Dyspnoea', 'Hoarseness', 'Wheezing', 'Chest_pain', 'Exercise_tolerance', 'Swelling', 'Weight_loss'],
                'cardiovascular': ['Dyspnoea', 'Paroxysmal_nocturnal_dyspnoea', 'Orthopnoea', 'Chest_pain', 'Palpitations', 'Ankle_swelling', 'Dizziness', 'Limb_pain', 'Walking_distance', 'Colour_changes_in_hands_and_feet', 'Weight_loss'],
                'urinary': ['Loin pain', 'Frequency_of_micturition', 'nocturnal_frequency', 'Poor stream', 'Dribbling', 'Hesitancy', 'Dysuria', 'Urgency', 'Precipitancy', 'Painful micturition', 'Polyuria', 'Thirst', 'Haematuria', 'Incontinence', 'Swelling', 'Weight_loss', 'Feeling_of_Incomplete_Voiding'],
                'reproduction_f': ['Dyspareunia', 'menarche', 'menopause', 'Frequency', 'Quantity', 'duration_of_menstruation', 'Vaginal_discharge', 'Dysmenorrhoea', 'Previous_pregnancies', 'complication_of_previous_pregnancies', 'Prolapse', 'Urinary_incontinence', 'Breast_pain', 'Nipple_discharge', 'Lumps', 'Skin_changes', 'Swelling', 'Weight_loss', 'Vaginal_discharge'],
                'reproduction_m': ['impotence', 'incontinence', 'Weight_loss', 'Discharge'],
                'nervous': ['Changes_of_behaviour', 'Depression', 'Memory_loss', 'Delusions', 'Anxiety', 'Tremor', 'Syncopal_attacks', 'Loss_of_consciousness', 'Fits', 'Muscle_weakness', 'Paralysis', 'Sensory disturbances', 'Paraesthesias', 'Dizziness', 'Changes_of_smell', 'Changes_of_vision', 'Changes_of_hearing', 'Tinnitus', 'Headaches', 'Swelling', 'Weight_loss'],
                'musculoskeletal': ['Aches_or_pains_in_muscles_or_bones_or_joints', 'Swelling_joints', 'Limitation_of_joint_movements', 'Locking', 'Weakness', 'Disturbances_of_gait', 'Swelling', 'Wasting']
                }
        for symptom in Complaint.pc.keys():
            the_five_cs = ['complaint', 'cause', 'course', 'complication', 'care_so_far']
            # analyze the symptom
            for cee in the_five_cs:
                if cee == "complaint":
                    Complaint.hpc[cee] = symptom
                else:
                    Complaint.hpc[cee] = input(f"Write on the [{colored(cee, 'blue')}] of this symptom =>  ")
            

            data = list(direct_questions.keys())
            column = ['Index', "System List"]
            myTab = PrettyTable()

            # Add Columns
            myTab.add_column(column[0], [index for index in range(len(data))])
            myTab.add_column(column[1], data)
            print(myTab)

            while (system := input(f"\nWrite the system this symptom [{colored(symptom, 'blue')}] affects => ")) != "":
                if system in direct_questions.keys():
                    Utils.print_center(colored("Systematic direct questions", 'green'))
                    for system_symptom in direct_questions[system]:
                        response = input(f"Enter in details the history of this symptom if present [{colored(system_symptom, 'blue')}] => ")
                        if response != '' and Utils.checkLine(system_symptom):
                            catch = Utils.checkLine(system_symptom)
                            Complaint.hpc[system_symptom] = xterize(catch)
                        else:
                            Complaint.hpc[system_symptom] = response
                else:
                    print(colored("System not in the list, spell correctly in small letters", "black", "on_red"))


        self.history_of_complaint = Complaint.hpc
