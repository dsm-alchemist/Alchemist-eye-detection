# Import Library
import torchvision
from load_model import load_model
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

# Load Model
model = load_model(2)

# 클래스를 새로운 것으로 바꿉니다.
num_classes = 2     # 1 class (person) + background
# 분류기의 input feature의 개수를 가져옵니다.
in_features = model.roi_heads.box_predictor.cls_score.in_features
# pretrain
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)