# Import Library
import torch
import torchvision
from torchvision import models
import torchvision.transforms as T
from parameter import IMG_SIZE, COLORS, THRESHOLD
from load_model import load_model
from torchvision import transforms as T
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

""" human segmentation은 posture classification의 input image가 될 것 입니다. """

