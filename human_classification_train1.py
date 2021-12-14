# Import Library
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision import models
from human_classification_model import train_model
from parameter import default_path

def model_train():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model_conv = models.resnet18(pretrained=True)
    for param in model_conv.parameters():
        param.requires_grad = False

    # 새로 생성된 모듈의 매개변수는 기본값이 requires_grad=True 임
    num_ftrs = model_conv.fc.in_features
    model_conv.fc = nn.Linear(num_ftrs, 2)

    model_conv = model_conv.to(device)

    criterion = nn.CrossEntropyLoss()

    # 이전과는 다르게 마지막 계층의 매개변수들만 최적화되는지 관찰
    optimizer_conv = optim.SGD(model_conv.fc.parameters(), lr=0.01, momentum=0.9)

    # 7 에폭마다 0.1씩 학습률 감소
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_conv, step_size=7, gamma=0.1)

    model_conv = train_model(model_conv, criterion, optimizer_conv, exp_lr_scheduler, num_epochs=25)
    return model_conv

if __name__ == '__main__':
    model = model_train()
    torch.save(model.state_dict(), default_path + '/model/classification_1.pt')