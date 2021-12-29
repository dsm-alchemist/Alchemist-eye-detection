# Import Library
import torch
import torchvision.transforms as T
from segmentation.instance_segmentation import instance_segmentation
from human_classification_model import CNN
from parameter import default_path

# Segmentation을 이용해 Input 값으로 넣고 분류 결과를 알려준다.
def posture_classification(img_path, url=False):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    classes = ['lying', 'sitting']
    model = CNN(len(classes))

    img = instance_segmentation(path=img_path, threshold=0.70, url=url)
    model.load_state_dict(torch.load(default_path + '/model/classification_model.pth', map_location=device))
    model.eval()

    transform = T.Compose([T.ToPILImage(), T.Resize((128, 128)), T.ToTensor()])
    img = transform(img).unsqueeze(dim=0)

    pred = model(img).to(device)
    _, preds = torch.max(pred, 1)

    if preds[0] == 1:
        return "break"
    else:
        return "run"