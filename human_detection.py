# Import Library
from torchvision import models
import torchvision.transforms as T
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# Download Model : https://pytorch.org/vision/stable/models.html
model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()

def human_detection(path_1, path_2, path_3, path_4, path_5):
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

    # 사람의 위치 좌표
    """
    리스트 0~1 : 1번 이미지
    리스트 2~3 : 2번 이미지
    리스트 4~5 : 3번 이미지
    리스트 6~7 : 4번 이미지
    리스트 8~9 : 5번 이미지
    """
    x_coo = []
    y_coo = []

    for i in range(0, 5):
        path = path_list[i]
        # img_path = './data/demo/sleep_1.JPG'
        img = Image.open(path)
        # img = img.transpose(Image.ROTATE_270)
        img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

        # 이미지를 텐서로 바꿔주기
        trf = T.Compose([T.ToTensor()])   # 이미지를 0~1의 값을 값는 텐서로 변경
        input_img = trf(img)
        # print(input_img.shape)  # [채널, 세로, 가로]

        try:
            # Inference
            out = model([input_img])[0]
            # print(out.keys())
            """
            dict_keys(['boxes', 'labels', 'scores', 'keypoints', 'keypoints_scores'])
            우리는 boxes score를 사용하겠다.
            """
        except:
            # print("사람이 감지되지 않았습니다.")
            return False
        else:
            # Visualization
            codes = [
                Path.MOVETO,
                Path.LINETO,
                Path.LINETO
            ]
            fig, ax = plt.subplots(1, figsize=(16, 16))

            for box, score in zip(out['boxes'], out['scores']):
                score = score.detach().numpy()

                if score < THRESHOLD:
                    continue

                box = box.detach().numpy()
                rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='b', facecolor='none')
                ax.add_patch(rect)
                print('사람이 있음.')
                # ax.imshow(img)
                #plt.show()

                # 0~1 : X좌표 | 2~3 : Y좌표
                x_coo.append(box[0])
                x_coo.append(box[1])
                y_coo.append(box[2])
                y_coo.append(box[3])

                print(x_coo)
                print(y_coo)

            return x_coo, y_coo

human_detection('./data/demo/study_1.JPG', './data/demo/study_2.JPG', './data/demo/study_3.JPG', './data/demo/study_4.JPG', './data/demo/two_study.jpeg')