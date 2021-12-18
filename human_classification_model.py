# Import Library
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)  # 합성곱 연산 (입력 채널 수: 3, 출력 채널 수: 6, 필터 크기: 5x5, stride=1(default))
        self.pool1 = nn.MaxPool2d(2, 2)  # 합성곱 연산 (필터크기 2x2, stride=2)
        self.conv2 = nn.Conv2d(6, 16, 5)  # 합성곱 연산 (입력 채널 수: 6, 출력 채널수: 16, 필터 크기: 5x5, stride=1(default))
        self.pool2 = nn.MaxPool2d(2, 2)  # 합성곱 연산 (필터크기 2x2, stride=2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)  # 5x5 피쳐맵 16개를 일렬로 피면 16*5*5개의 노드가 생성됨.
        self.fc2 = nn.Linear(120, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))  # conv1 -> ReLU -> pool1
        x = self.pool2(F.relu(self.conv2(x)))  # conv2 -> ReLU -> pool2

        x = x.view(-1, 16 * 5 * 5)  # 5x5 피쳐맵 16개를 일렬로 만든다.
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        return x