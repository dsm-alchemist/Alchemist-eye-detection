# Import Library
import torch
import torch.nn as nn
from torchvision import transforms
from torch.utils.data import DataLoader
from human_classification_model import CNN
from human_classification_dataloader import CustomImageDataset
from human_classification_loss_graph import g_show
from parameter import default_path

def train():
    torch.multiprocessing.freeze_support()

    # Device 설정
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f'Your Device : {device}\n')

    epoch_num = 20
    batch_num = 8
    lr_num = 1e-3
    loss_train = []
    loss_test = []

    transforms_train = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()])

    transforms_test = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()])

    train_data_set = CustomImageDataset(data_set_path=default_path+'/data/train', transforms=transforms_train)
    train_loader = DataLoader(train_data_set, batch_size=batch_num, shuffle=True)

    test_data_set = CustomImageDataset(data_set_path=default_path+'/data/val', transforms=transforms_test)
    test_loader = DataLoader(test_data_set, batch_size=batch_num, shuffle=True)

    if not (train_data_set.num_classes == test_data_set.num_classes):
        print("error: Numbers of class in training set and test set are not equal")
        exit()

    num_classes = train_data_set.num_classes
    custom_model = CNN(num_classes=num_classes).to(device)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(custom_model.parameters(), lr=lr_num)

    for e in range(epoch_num):
        for i_batch, item in enumerate(train_loader):
            images = item['image'].to(device)
            labels = item['label'].to(device)

            # Forward pass
            outputs = custom_model(images)
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i_batch + 1) % batch_num == 0:
                print('Epoch [{}/{}], Loss: {:.4f}'
                    .format(e + 1, epoch_num, loss.item()))

    # Test the model
    custom_model.eval()  # eval mode (batchnorm uses moving mean/variance instead of mini-batch mean/variance)
    with torch.no_grad():
        correct = 0
        total = 0
        for item in test_loader:
            images = item['image'].to(device)
            labels = item['label'].to(device)
            outputs = custom_model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += len(labels)
            correct += (predicted == labels).sum().item()

        print('Test Accuracy of the model on the {} test images: {} %'.format(total, 100 * correct / total))


    g_show(loss_train, loss_test, 'Loss', 'classification_loss')

    # 모델 저장 경로
    PATH = default_path + '/model/classification_model.pth'
    torch.save(custom_model.state_dict(), PATH)  # 모델 저장

if __name__ == '__main__':
    train()