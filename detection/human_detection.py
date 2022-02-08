# Import Library
import torch
from torchvision.transforms import transforms as T
from PIL import Image
from detection.return_detect import return_detect
from parameter import THRESHOLD
from parameter import default_path

# 이미지 Size
IMG_SIZE = 480
PATH = f'{default_path}/models/detection.pth'
model = torch.load(PATH).eval()

def human_detection(args):
    try:
        if args:
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
        else:
            return False
    except:
        return False