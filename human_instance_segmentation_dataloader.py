# Import Library
import os
import numpy as np
import torch
from PIL import Image



""" human segmentation은 posture classification의 input image가 될 것 입니다. """

class human_segmentation(torch.utils.data.Dataset):
    def __init__(self, root, transforms):
        self.root = root
        self.transforms = transforms
        self.imgs = list(sorted(os.listdir(os.path.join(root+'data/', "PNGImages"))))
        self.masks = list(sorted(os.listdir(os.path.join(root+'data/', "PedMasks"))))

    def __getitem__(self, idx):
        # Load images and masks
        img_path = os.path.join(self.root, "PNGImages", self.imgs[idx])
        mask_path = os.path.join(self.root, "PedMasks", self.masks[idx])
        img = Image.open(img_path).convert("RGB")

        # 각 색상은 0인 다른 인스턴스에 해당하기 때문에 masks를 RGB로 변환하지 않았다.
        mask = Image.open(mask_path)
        # 이미지를 숫자배열로 변환
        mask = np.array(mask)
        # 인스턴스가 다른색으로 incoding 됨
        obj_ids = np.unique(mask)
        # 첫번째 ID = 배경 제거합니다.
        obj_ids = obj_ids[1:]

        # 색 mask를 binary 이진 마스크로 분할
        masks = mask == obj_ids[:, None, None]


