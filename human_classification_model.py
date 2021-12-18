# Import Library
import torch
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt

class Net(nn.Module):
    # Device 설정
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f'Your Device : {device}\n')

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)         # 합성곱 연산 (입력 채널 수 : 3, 출력 채널 수 : 6, 필터 크기 : 5x5, stride=1 (default))
        self.pool1 = nn.MaxPool2d(6, 16, 5)     # 합성곱 연산 (필터 크기 : 2x2, stride=2)
        self.conv2 = nn.Conv2d(6, 16, 5)        # 합성곱 연산 (입력 채널 수 : 8, 출력 채널 수 : 16, 필터 크기 : 5x5, stride=1 (default))
        self.pool2 = nn.MaxPool2d(6, 16, 5)     # 합성곱 연산 (필터 크기 : 2x2, stride=2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)   # 5x5 피쳐맵 18개를 일렬로 피면 16*5*5개의 노드를 생성됨.
        self.fc2 = nn.Linear(120, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))   # conv1 -> ReLU -> pool1