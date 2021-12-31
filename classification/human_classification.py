# Import Library
from classification.posture_classification import posture_classification

def human_classification(*args) -> bool:
    """
    :param args: images (only 5)
    :return: bool, if True, loop timer; False, timer is stopped;
    """
    run_num = 0
    break_num = 0

    results = [posture_classification(arg) for arg in args]

    # TODO: Refactor
    for img_result in results:
        if img_result == 'run':
            run_num += 1
        else:
            break_num += 1

    if run_num > break_num:
        return True
    else:
        return False