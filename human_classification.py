# Import Library
import torch
import torchvision.transforms as T
from instance_segmentation import instance_segmentation
from human_classification_model import CNN
from parameter import default_path

def posture_classification(img_path, url=False):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    classes = ['lying', 'sitting']
    model = CNN(len(classes))

    img = instance_segmentation(default_path + '/data/demo/study_3.JPG')
    model.load_state_dict(torch.load(default_path + '/model/classification_model.pth', map_location=device))
    model.eval()

    transform = T.Compose([T.ToPILImage(), T.Resize((128, 128)), T.ToTensor()])
    img = transform(img).unsqueeze(dim=0)

    pred = model(img).to(device)
    _, preds = torch.max(pred, 1)

    if preds == preds[0]:
        return 'break'
    else:
        return 'run'