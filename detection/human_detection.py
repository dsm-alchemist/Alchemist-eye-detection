# Import Library
import torchvision.transforms as T
from PIL import Image
from detection.return_detect import return_detect
from load_model import load_model
from parameter import THRESHOLD

# 이미지 Size
IMG_SIZE = 480
model = load_model(0)

def human_detection(args):
    try:
        for path in args:
            img = Image.open(path)
            img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

            # 이미지를 텐서로 바꿔주기
            trf = T.Compose([T.ToTensor()])   # 이미지를 0~1의 값을 값는 텐서로 변경
            input_img = trf(img)

            if return_detect(model=model, input_img=input_img, THRESHOLD=THRESHOLD):
                continue
            else:
                return False
        return True
    except:
        return False