# Import Library
from __future__ import print_function, division
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
from parameter import default_path

def train_model(model, criterion, optimizer, cheduler, num_epochs=25):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print(f"Epoch {epoch} / {num_epochs - 1}")
        print('-' * 10)

        # 각 epoch은 train 단계와 test 단계를 갖습니다.
        for phase in ['train', 'test']:
            if phase == 'train':
                model.train()   # 모델을 학습 모드로 설정
            else:
                model.eval()    # 모델을 평가 모드로 설정

            running_loss = 0.0
            running_corrects = 0