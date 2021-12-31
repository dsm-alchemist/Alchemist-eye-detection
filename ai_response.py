# Import Library
from detection.human_detection import human_detection
from classification.human_classification import human_classification
from classification_2.human_classification2 import human_classification2

def ai_response(*args):
    if not human_detection(*args):
        return False
    elif not human_classification(*args):
        return human_classification2(*args)
    else:
        return True