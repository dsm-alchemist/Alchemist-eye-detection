# Import Library
import torchvision.transforms as T
from PIL import Image
from return_detect import return_detect
from load_model import load_model
from parameter import IMG_SIZE, THRESHOLD
import requests
from io import BytesIO
from get_path import get_path

def human_detect(path_1, path_2, path_3, path_4, path_5, url=False):
    model = load_model(0)

    # 이미지 path 리스트
    path_list = get_path(path_1, path_2, path_3, path_4, path_5)

    for i in range(0, 5):
        if url:
            response = requests.get(path_list[i])
            img = Image.open(BytesIO(response.content))
        else:
            path = path_list[i]
            img = Image.open(path)

        img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

        # 이미지를 텐서로 바꿔주기
        trf = T.Compose([T.ToTensor()])   # 이미지를 0~1의 값을 값는 텐서로 변경
        input_img = trf(img)
        # print(input_img.shape)  # [채널, 세로, 가로]
        if return_detect(model, input_img, THRESHOLD) == False:
            return 'NO_HUMAN'
        else:
            pass
    return True