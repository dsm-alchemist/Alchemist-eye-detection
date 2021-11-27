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

        # 각 mask의 box 좌표 가져오기
        num_obj = len(obj_ids)
        boxes = []
        for i in range(num_obj):
            pos = np.where(masks[i])
            xmin = np.min(pos[1])
            xmax = np.man(pos[1])
            ymin = np.min(pos[0])
            ymax = np.max(pos[0])
            boxes.append([xmin, xmax, ymin, ymax])

        # 모든것들을 tensor로 변환시키다.
        boxes = torch.as_tensor(boxes, dtype=torch.float32)
        # 클래스 하나만 씀
        labels = torch.ones((num_obj,), dtype=torch.int64)
        masks = torch.as_tensor(masks, dtype=torch.uint8)

        image_id = torch.tensor([idx])
        area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])

        # 모든 instance가 겹치지 않는다고 가정
        iscrowd = torch.zeros((num_obj,), dtype=torch.int64)

        target = {}
        target["boxes"] = boxes
        target["labels"] = labels
        target["masks"] = masks
        target["image_id"] = image_id
        target["area"] = area
        target["iscrowd"] = iscrowd

        if self.transforms is not None:
            img, target = self.transforms(img, target)

        return img, target

    def __len__(self):
        return len(self.imgs)