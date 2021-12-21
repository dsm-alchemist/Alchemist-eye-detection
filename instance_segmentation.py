from instance_segmentation_model import instance_segmentation_model
from get_path import get_path

def instance_segmentation(path, threshold=0.95, url=False):
    img, _, _ = instance_segmentation_model(path, threshold, url)

    return img