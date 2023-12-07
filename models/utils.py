import shutil
import sys

class Utils:
    def __init__(self):
        ...

    @staticmethod
    def print_center(s):
        terminal_width = shutil.get_terminal_size().columns
        centered_text = s.center(terminal_width)
        print(centered_text)

    @staticmethod
    def checkLine(text):
        symptoms = ['pain', 'swelling', 'vomit', 'bleeding']
        result = ''

        for symptom in symptoms:
            if symptom in text.lower():
                result = symptom
                break
        return result if len(result) else None

    @staticmethod
    def safeInput(text):
        try:
            var = input(text)
            return var
        except (KeyboardInterrupt, EOFError):
            print("\nYou are about to terminate a session, all data will be lost if you continue")
            try:
                var = input("Would you like to exit this session anyway?! Y/N => ")
                if var.lower() == "y":
                    print("Session ended")
                    sys.exit()
                while var.lower() != "n":
                    print("Type either Y/N")
            except (KeyboardInterrupt, EOFError):
                print("Session ended")
                sys.exit()
