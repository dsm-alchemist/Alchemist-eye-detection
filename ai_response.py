# Import Library
from detection.human_detection import human_detection
from classification.human_classification import human_classification

def ai_response(*args):
    if not human_detection(*args):
        return False
    return human_classification(*args)