# Import Library
from detection.human_detection import human_detection
from classification_2.human_classification2 import human_classification2

def ai_response(*args):
    if not human_detection(*args):
        return False
    else:
        return human_classification2(*args)