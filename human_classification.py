# Import Library
import torch
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from human_classification_model import CNN

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
model = CNN(num_classes=2).to(device)

