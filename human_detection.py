# Import Library
from torchvision import models
import torchvision.transforms as T
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# Download Model : https://pytorch.org/vision/stable/models.html
model = models.detection.keypointrcnn_resnet50_fpn(pretrained=True).eval()
"""
class human_detecion:
    def __init__(self, imgs_path=None):
        self.IMG_SIZE = 480
        # 95% 이상이 되어야 사람으로 Detect
        self.THRESHOLD = 0.95
        self.imgs = imgs_path

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, item):
        # 이미지 확인
        # plt.figure(figsize=(16, 16))
        # plt.imshow(self.img)
        # plt.show()
        # Load Image
        self.img = Image.open(imgs)
        self.img = self.img.transpose(Image.ROTATE_270)
        self.img = self.img.resize((self.IMG_SIZE, int(self.img.height * self.IMG_SIZE / self.img.width)))
"""
img_path = './data/demo/study_1.JPG'
IMG_SIZE = 480
# 95% 이상이 되어야 사람으로 Detect
THRESHOLD = 0.95
path = img_path
# img_path = './data/demo/sleep_1.JPG'
img = Image.open(path)
img = img.transpose(Image.ROTATE_270)
img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

# 이미지를 텐서로 바꿔주기
trf = T.Compose([T.ToTensor()])   # 이미지를 0~1의 값을 값는 텐서로 변경
input_img = trf(img)
# print(input_img.shape)  # [채널, 세로, 가로]
ㄴ
try:
    # Inference
    out = model([input_img])[0]
    # print(out.keys())
    """
    dict_keys(['boxes', 'labels', 'scores', 'keypoints', 'keypoints_scores'])
    우리는 boxes score를 사용하겠다.
    """
except:
    print("사람이 없습니다")
else:
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO
    ]
    fig, ax = plt.subplots(1, figsize=(16, 16))

    # Visualization
    for box, score in zip(out['boxes'], out['scores']):
        score = score.detach().numpy()

        if score < THRESHOLD:
            continue

        box = box.detach().numpy()
        rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='b', facecolor='none')
        ax.add_patch(rect)
        print('사람이 있음.')
        ax.imshow(img)
        plt.show()