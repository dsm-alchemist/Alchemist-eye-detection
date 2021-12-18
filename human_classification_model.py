# Import Library
import torch.nn as nn
import torch.nn.functional as F

batch_size = 8

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()  # Super class로 지금 작성하고있는 클래스 자체를 초기화하기 위함
        self.layer = nn.Sequential(
            nn.Conv2d(1, 16, 5),
            nn.ReLU(),
            nn.Conv2d(16, 32, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2))
        # Conv2d : Convolution Filtering이라는 Signal Processing적인 방법으로 이미지를 처리 하는것으로,
        # nn.Conv2d(1,16,5)는 1개필터짜리 입력(28x28 해상도의 이미지, default filter 갯수 = 1)을 받아 16개의 필터로 size 5의 Kernel(Filtering)을 하는것입니다.
        # 기본적으로 CNN은 신호/영상처리에 대한 기본적인 이해가 있어야합니다.
        # Kernel size가 5인경우, Convoltuion을 하게 되면 4개의 pixel이 사라지게 되어(28x28)의 input 이미지가 (24x24)가 됩니다.
        # 이런식으로 이미지의 사이즈를 줄여가며 강한 특징만을 추려나가는게 CNN입니다.
        # MaxPooling을 중간중간 섞어줌으로써, Convolution보다 더욱 강하게 Feature들을 뽑아내줍니다.

        self.fc_layer = nn.Sequential(
            nn.Linear(64 * 3 * 3, 100),
            nn.ReLU(),
            nn.Linear(100, 10))
        # self.layer : CNN이 끝난 이후, 최종적으로 나오는 결과물은 [batch_size,64,3,3]입니다.
        # 즉, 256개의 이미지 묶음씩 64개의 필터, (3x3)의 이미지가 남게 되는것으로, pixel갯수로 따지면 64*3*3이 나오게 되는것입니다.
        # 따라서, 64*3*3의 결과값을 nn.Linear(100,10)을 통해 최종적으로 10개의 값이 나오게하는데
        # 이 10개의 값이 내가 넣은 이미지가 0~9(10개)중 어떤것일지에 대한 각각의 확률입니다.

    def forward(self, x):
        out = self.layer(x)
        out = out.view(batch_size, -1)
        out = self.fc_layer(out)
        return out
        # CNN함수의 전체적인 그림으로, Conv2d -> Linear Regression -> 추정 입니다.