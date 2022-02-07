# Import Library
from detection.human_detection import human_detection

def ai_response(args):
    result = human_detection(args)
    print(f"ai_response : {result}")
    return result