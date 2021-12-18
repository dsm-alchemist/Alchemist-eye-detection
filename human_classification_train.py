# Import Library
import torch
import torch.nn as nn
import torch.optim as optim
from human_classification_model import CNN
from human_classification_dataloader import trainloader, testloader
from human_classification_loss_graph import g_show
from parameter import default_path

def train():
    torch.multiprocessing.freeze_support()
    # Device 설정
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f'Your Device : {device}\n')

    loss_ = []  # loss 저장용 리스트
    num_epoch = len(trainloader)  # 배치개수
    model = CNN().to(device)  # 모델 선언
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=1e-3)

    print(model)
    # 피쳐맵은 다음과 같이 바뀌면서 진행된다. 32 -> 28 -> 14 -> 14 -> 5

    for i in range(num_epoch):
        for j, [image, label] in enumerate(trainloader):
            x = image.to(device)
            # x = x.permute(0, 3, 1, 2)
            y_ = label.to(device)

            optimizer.zero_grad()   # optimizer 초기화
            output = model.forward(x)   # 학습용 데이터로 CNN 실시
            loss = criterion(output, y_)    # 학습해서 추정해낸 값과, 실제 라벨된 값 비교
            loss.backward()     # 오차만큼 다시 Back Propagation 시행
            optimizer.step()    # Back Propagation시 ADAM optimizer 매 Step마다 시행

            if j % 1000 == 0:
                print(loss)
                loss_.append(loss.cpu().detach().numpy())

    correct = 0
    total = 0

    with torch.no_grad():
        for image, label in testloader:
            x = image.to(device)
            y_ = label.to(device)

            output = model.forward(x)
            _, output_index = torch.max(output, 1)

            total += label.size(0)
            correct += (output_index == y_).sum().float()

        print("Accuracy of Test Data : {}".format(100 * correct / total))

    g_show(loss_, 'Train Loss', 'classification_loss')

    # 모델 저장 경로
    PATH = default_path + '/model/classification_model.pth'
    torch.save(CNN.state_dict(), PATH)  # 모델 저장

if __name__ == '__main__':
    train()