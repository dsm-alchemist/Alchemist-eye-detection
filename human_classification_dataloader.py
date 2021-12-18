# Import Library
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms
from parameter import default_path

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

trainset = torchvision.datasets.ImageFolder(root=default_path + '/data/train', transform=transform)
testset = torchvision.datasets.ImageFolder(root=default_path + '/data/test', transform=transform)

trainloader = DataLoader(trainset, batch_size=8, shuffle=False)
testloader = DataLoader(testset, batch_size=8, shuffle=False)

""" # Class 확인
classes = trainset.classes    # ['lying', 'sitting']
print(classes) """