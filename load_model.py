from torchvision import models

def load_model(model_num):
    # Download Model : https://pytorch.org/vision/stable/models.html
    if model_num == 0:
        model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()
        return model
    elif model_num == 1:
        model = models.detection.maskrcnn_resnet50_fpn(pretrained=True).eval()
        return model
    elif model_num == 2:
        return False
    else:
        print("모델이 없습니다.")
        print("detection : 0 | segmentation : 1 | classification : 2")