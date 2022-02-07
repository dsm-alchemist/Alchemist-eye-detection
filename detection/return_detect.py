# Import Library
from parameter import THRESHOLD

def return_detect(model, input_img, THRESHOLD=THRESHOLD):
    out = model([input_img])[0]
    try:
        for box, score, keypoints in zip(out['boxes'], out['scores'], out['keypoints']):
            score = score.detach().numpy()

            if score < THRESHOLD:
                continue
            else:
                return True
    except:
        return False