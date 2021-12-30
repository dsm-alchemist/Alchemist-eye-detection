# Import Library
from PIL import Image
from segmentation.color_mask import color_masks
from segmentation.segmentation_predict import get_prediction
import cv2
from urllib.request import urlopen
import numpy as np
from parameter import white

# URL로 받아올 경우 이미지로 변환해주는 함수
def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    return image

# Instance Segmenatation 함
def instance_segmentation_model(img, threshold=0.7,):
    masks, pred_cls = get_prediction(img, threshold=threshold)
    for i in range(len(masks)):
        img = cv2.cvtColor(np.array(Image.open(img)), cv2.COLOR_BGR2RGB) # For working with RGB images instead of BGR
        white_img = cv2.imread(white)

        for i in range(len(masks)):
            try:
                if pred_cls[i] == 'human':
                    rgb_mask = color_masks(masks[i])
                    img = cv2.addWeighted(img, 0, rgb_mask, 1, 0)
                    # img = img.copy()
                    # img = 255-img
                    return img, pred_cls, masks[i]
                else:
                    pass
            except:
                rgb_mask = color_masks(masks[i])
                img = cv2.addWeighted(white_img, 0, rgb_mask, 1, 0)
                return img, pred_cls, masks[i]