from instance_segmentation_model import instance_segmentation_model
import matplotlib.pyplot as plt

in_img = './data/demo/study_1.JPG'

img, sdv, mask = instance_segmentation_model(in_img)

print(sdv)

plt.imshow(img)
plt.show()