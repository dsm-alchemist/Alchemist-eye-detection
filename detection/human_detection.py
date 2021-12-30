# Import Library
import torchvision.transforms as T
from PIL import Image
from detection.return_detect import return_detect
from load_model import load_model
from parameter import IMG_SIZE

def human_detection(*args):
    model = load_model(0)
    for path in args:
        img = Image.open(path)
        img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

        # 이미지를 텐서로 바꿔주기
        trf = T.Compose([T.ToTensor()])   # 이미지를 0~1의 값을 값는 텐서로 변경
        input_img = trf(img)
        if not return_detect(model, img, input_img, THRESHOLD=0.65):
            return False
    return True