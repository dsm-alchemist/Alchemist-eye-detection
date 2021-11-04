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

# Download Model : https://pytorch.org/docs/stable/torchvision/models.html
model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()

# Load Image
img = Image.open('../data/')

# 3분 48초