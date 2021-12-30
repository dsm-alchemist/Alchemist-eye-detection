# Import Library
from parameter import COCO_INSTANCE_CATEGORY_NAMES
from torchvision import transforms as T
from PIL import Image
from load_model import load_model

def get_prediction(img_path, threshold=0.7):
    model = load_model(2)
    img = Image.open(img_path)
    transform = T.Compose([T.ToTensor()])
    img = transform(img)
    img = img.cpu()
    # img = img.gpu()
    pred = model([img])

    pred_score = list(pred[0]['scores'].detach().cpu().numpy())
    pred_t = [pred_score.index(x) for x in pred_score if x > threshold][-1]

    masks = (pred[0]['masks'] > 0.7).squeeze().detach().cpu().numpy()
    pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in list(pred[0]['labels'].cpu().numpy())]
    masks = masks[:pred_t + 1]
    pred_class = pred_class[:pred_t + 1]
    return masks, pred_class