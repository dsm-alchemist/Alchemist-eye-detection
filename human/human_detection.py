# Import Library
import torch
import torchvision
from torchvision import models
import torchvision.transforms as T
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.path import Path
import matplotlib.patches as patches

IMG_SIZE = 480
# 95% 이상이 되어야 사람으로 Detect
THRESHOLD = 0.95

# Download Model : https://pytorch.org/vision/stable/models.html
model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()

# Load Image
img = Image.open('../data/demo/study_1.JPG')
img = img.transpose(Image.ROTATE_270)
img = img.resize((IMG_SIZE, int (img.height * IMG_SIZE / img.width)))

## 이미지 확인
"""
plt.figure(figsize=(16, 16))
plt.imshow(img)
plt.show()
"""

# 이미지를 텐서로 바꿔주기
trf = T.Compose([T.ToTensor()])   # 이미지를 0~1의 값을 값는 텐서로 변경
input_img = trf(img)
print(input_img.shape)  # [채널, 세로, 가로]

# Inference
out = model([input_img])[0]
print(out.keys())
"""
dict_keys(['boxes', 'labels', 'scores', 'keypoints', 'keypoints_scores'])
우리는 boxes score를 사용하겠다.
"""

# Visualization
for box, score in zip(out['boxes'], out['scores']):
    score = score.detach().numpy()

    if score < THRESHOLD:
        continue

