# Import Library
from segmentation.instance_segmentation_model import instance_segmentation_model

def instance_segmentation(path, threshold=0.65):
    img, _, _ = instance_segmentation_model(img=path, threshold=threshold)

    return img