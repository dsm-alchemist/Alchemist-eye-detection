# Import Library
from torchvision import models
import torchvision.transforms as T
from PIL import Image
from return_detect import return_detect

def human_detect(path_1, path_2, path_3, path_4, path_5):
    # Download Model : https://pytorch.org/vision/stable/models.html
    model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()

    IMG_SIZE = 480
    # 95% 이상이 되어야 사람으로 Detect
    THRESHOLD = 0.95

    # 이미지 path 리스트
    path_list = []
    path_list.append(path_1)
    path_list.append(path_2)
    path_list.append(path_3)
    path_list.append(path_4)
    path_list.append(path_5)

    for i in range(0, 5):
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

human_detect('./data/demo/study_4.JPG', './data/demo/study_3.JPG', './data/demo/study_2.JPG', './data/demo/sleep_1.JPG', './data/demo/no_human.png')