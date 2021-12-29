# Import Library
from instance_segmentation_model import instance_segmentation_model

def instance_segmentation(path, threshold=0.70, url=False):
    img, _, _ = instance_segmentation_model(img_path=path, threshold=threshold, url=url)

    return img