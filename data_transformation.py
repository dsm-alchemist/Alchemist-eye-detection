# Import Library
from instance_segmentation import instance_segmentation
from parameter import default_path
import numpy as np
from PIL import Image
import os

option = 'sitting'

# file_path = default_path + '/data/' + str(option) + '/'
file_path = default_path + '/data/train/' + str(option) + '/'
file_names = os.listdir(file_path)

print(f"파일 개수 : {len(file_names)}")

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = option + '_' + str(i) + '.JPG'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

file_names = os.listdir(file_path)
print(file_names)

# AI용 이미지 만들기
count = 0
for num in file_names:
    try:
        img = instance_segmentation(default_path + '/data/' + option + '/' + file_names[count])
        img_copy = img.copy()
        img_copy = np.array(img_copy)
        result = Image.fromarray(img_copy)

        if count <= 350:
            result.save(default_path + '/data/train/' + option + '/' + option + '_' + str(count + 1) + '.JPG')
            count += 1
        elif count > 350:
            result.save(default_path + '/data/train/' + option + '/' + option + '_' + str(count + 1) + '.JPG')
            count += 1
    except:
        count += 1
        pass


""" 크롤링 오류 데이터 삭제
file_error = [1, 7, 26, 27, 32, 34, 45, 50, 54, 63, 69, 80, 82, 86, 97, 102, 104, 116, 118, 130, 139, 143, 165, 170, 176, 178, 190, 199, 204, 205, 210, 217, 218, 228, 231, 241, 251, 255, 258, 271, 273, 289, 292, 295, 302, 311, 312, 315, 316, 326, 328, 335, 337, 357, 364, 366, 380, 403, 405, 411, 424, 425, 426, 429, 435, 438, 440, 444, 458, 464, 468, 480, 485, 488, 493, 497, 498, 502, 504, 509, 518]

count = 0
for i in file_error:
    file = file_path + file_names[file_error[count]]

    if os.path.isfile(file):
        os.remove(file)
        count += 1
"""