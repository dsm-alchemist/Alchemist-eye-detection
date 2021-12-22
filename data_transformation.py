# Import Library
from instance_segmentation import instance_segmentation
from parameter import default_path
import numpy as np
from PIL import Image
import os

option = 'sitting'

file_path = default_path + '/data/' + str(option) + '/'
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

count = 0

for num in file_names:
    img = instance_segmentation(default_path + '/data/' + option + '/' + file_names[count])
    img_copy = img.copy()
    img_copy = np.array(img_copy)
    result = Image.fromarray(img_copy)

    if count <= 350:
        result.save(default_path + '/data/train/' + option + '/' + option +'_' + str(count+1) + '.JPG')
    else:
        result.save(default_path + '/data/train/' + option + '/' + option +'_' + str(count+1) + '.JPG')

    count += 1