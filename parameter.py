# Import Library
import numpy as np
import os

# Default Path
default_path = os.getcwd()

# 데이터 디렉토리
directory_list = [
    default_path + '/data/train/',
    default_path + '/data/test/',
    default_path + '/data/demo/'
]

# 이미지 Size
IMG_SIZE = 480

# 정확도
THRESHOLD = 0.95

# 사람은 검정, 사람을 제외한 나머지는 흰색
COLORS = np.array([
    (255, 255, 255),    # 0=background
    (255, 255, 255),    # 1=aeroplane
    (255, 255, 255),    # 2=bicycle
    (255, 255, 255),    # 3=bird
    (255, 255, 255),    # 4=boat
    (255, 255, 255),    # 5=bottle
    (255, 255, 255),    # 6=bus
    (255, 255, 255),    # 7=car
    (255, 255, 255),    # 8=cat
    (255, 255, 255),    # 9=chair
    (255, 255, 255),    # 10=cow
    (255, 255, 255),    # 11=dining table
    (255, 255, 255),    # 12=dog
    (255, 255, 255),    # 13=horse
    (255, 255, 255),    # 14=motorbike
    (0, 0, 0),          # 15=person
    (255, 255, 255),    # 16=potted plant
    (255, 255, 255),    # 17=sheep
    (255, 255, 255),    # 18=sofa
    (255, 255, 255),    # 19=train
    (255, 255, 255),    # 20=tv/monitor
])

study_1 = directory_list[2] + 'study_1.JPG'
study_2 = directory_list[2] + 'study_2.JPG'
study_3 = directory_list[2] + 'study_3.JPG'
study_4 = directory_list[2] + 'study_4.JPG'
study_5 = directory_list[2] + 'study_5.JPG'

study_list = [study_1, study_2, study_3, study_4, study_5]