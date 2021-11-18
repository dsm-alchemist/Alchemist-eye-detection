# Import Library
from torchvision import models
import torchvision.transforms as T
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import os, shutil

def human_detection(path_1, path_2, path_3, path_4, path_5):
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
        if RETURN(model, input_img, THRESHOLD) == False:
            return False
        else:
            pass
    return True

def RETURN(model, input_img, THRESHOLD):
    try:
        # Inference
        out = model([input_img])[0]
        # print(out.keys())
        """
        dict_keys(['boxes', 'labels', 'scores', 'keypoints', 'keypoints_scores'])
        우리는 boxes score를 사용하겠다.
        """
    except:
        return False
    else:
        # fig, ax = plt.subplots(1, figsize=(16, 16))

        for box, score in zip(out['boxes'], out['scores']):
            score = score.detach().numpy()

            # 사람일 확률
            if score < THRESHOLD:
                continue

            """ box 좌표
            box 0 : x1
            box 1 : y1
            box 2 : x2
            box 3 : y2 """
            # box = box.detach().numpy()

            """ 사람 그리기
            rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='b', facecolor='none')
            ax.add_patch(rect)
            ax.imshow(img)
            plt.show()
            """
            return True