# Import Library
import torch
import torchvision.transforms as T
from classification_2.human_classification2_model import CNN
from parameter import default_path
from PIL import Image

def posture_classification(img_path):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    classes = ['lying', 'sitting']
    model = CNN(len(classes))

    img = Image.open(img_path)

    model.load_state_dict(torch.load(default_path + '/models/classification2_model.pth', map_location=device))
    model.eval()

    transform = T.Compose([T.ToPILImage(), T.Resize((128, 128)), T.ToTensor()])
    img = transform(img).unsqueeze(dim=0)

    pred = model(img).to(device)
    _, preds = torch.max(pred, 1)

    if preds[0] == 1:
        return "break"
    else:
        return "run"