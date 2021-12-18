# Import Library
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from human_classification_model import Net
from human_classification_dataloader import trainloader
from parameter import default_path

def train():
    torch.multiprocessing.freeze_support()
    # Device 설정
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f'Your Device : {device}\n')

    net = Net().to(device)  # 모델 선언
    print(net)
    # 피쳐맵은 다음과 같이 바뀌면서 진행된다. 32 -> 28 -> 14 -> 14 -> 5

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=1e-3, momentum=0.9)

    loss_ = []  # loss 저장용 리스트
    n = len(trainloader)  # 배치개수

    for epoch in range(10):  # 10회 반복

        running_loss = 0.0

        for i, data in enumerate(trainloader, 0):
            inputs, labels = data[0].to(device), data[1].to(device)  # 배치 데이터

            optimizer.zero_grad()  # 배치마다 optimizer 초기화

            outputs = net(inputs)  # 노드 10개짜리 예측값 산출
            loss = criterion(outputs, labels)  # 크로스 엔트로피 손실함수 계산    optimizer.zero_grad() # 배치마다 optimizer 초기화
            loss.backward()  # 손실함수 기준 역전파
            optimizer.step()  # 가중치 최적화

            running_loss += loss.item()

            loss.backward()  # 손실함수 기준 역전파
            optimizer.step()  # 가중치 최적화

            running_loss += loss.item()

        loss_.append(running_loss / n)
        print('[%d] loss: %.3f' % (epoch + 1, running_loss / len(trainloader)))

    plt.plot(loss_)
    plt.title('Train Loss')
    plt.xlabel('epoch')
    plt.show()
    plt.savefig('/result/Train_Loss.png', dpi=300, facecolor='white')

    # 모델 저장 경로
    PATH = default_path + '/model/classification_model.pth'
    torch.save(net.state_dict(), PATH)  # 모델 저장

if __name__ == '__main__':
    train()