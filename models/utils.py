import shutil

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
