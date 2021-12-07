from instance_segmentation_model import instance_segmentation_model
from get_path import get_path

def instance_segementation(path_1, path_2, path_3, path_4, path_5, threshold=0.95, url=False):
    path_list = get_path(path_1, path_2, path_3, path_4, path_5)
    img_list = []

    for i in range(len(path_list)):
        img, pred_classes, masks = instance_segmentation_model(path_list[i], threshold, url)
        img_list.append(img)
    return img_list