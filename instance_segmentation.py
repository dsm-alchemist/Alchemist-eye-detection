from instance_segmentation_model import instance_segmentation_model

def instance_segmentation(path, threshold=0.95, url=False):
    img, _, _ = instance_segmentation_model(path, threshold, url)

    return img