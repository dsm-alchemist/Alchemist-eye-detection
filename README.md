# Alchemist-timer-stop-condition
Alchemist 서비스 중 하나인 타이머를 자동으로 멈춰주는 기능입니다.  
5분에 한번씩 5초 동안 5장의 사진을 찍어 첫번째로 사람을 detection 합니다.  
만약 사람이 없다면 타이머를 멈춥니다.  
두번째로 사람이 지금 누워있는지 일어나있는지 classification을 통해 누워있다면 타이머를 멈춥니다.

## Installation
```
# IF your device is mac os
% brew install libomp

# 가상환경은 도커를 사용합니다. 프로젝트 파일로 가서 아래 명령어를 실행해주세요.
% make run

# 도커 접속
% docker exec -it 컨테이너ID /bin/bash

# 도커 사용 해제
% make stop
```

# 작동 알고리즘
1. client에서 5초 동안 5장의 사진을 찍음.  
2. client에서 AI 호출.  
3. client에서 찍은 사진은 server로 전송.  
4. server에서 keypoint R-CNN이 사람을 detect.  
5. server에서 사람이 없다면 타이머 정지 (단 5개의 사진 모두 사람이 없어야 함).  
6. Input 이미지를 segmentation을 하여 사람만 검정 나머지는 흰색으로 output을 만들어 classification 모델의 Input 값으로 반환.  
7. server에서 사람이 있다면 일어나있는지 누워있는지 classification모델을 실행.  
8. 누워있다면 타이머 정지, 일어나 있다면 continue.

## Server
서버는 Flask를 사용했습니다.

# Reference

## Model
Human Detection Model은 Pytorch 공식 페이지에 있는 [Keypoint R-CNN](https://arxiv.org/abs/1703.06870)을 사용하였다.  
Human Segemtation Model은 Pytorch 튜토리얼에 있는 [Mask R-CNN](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)을 사용하였다.

## Data
Please download datum follow this [posture link](https://www.kaggle.com/deepshah16/silhouettes-of-human-posture?select=bending), [sitting human link](http://www2.informatik.uni-freiburg.de/~oliveira/dataset.html).  
data label은 bending, lying, sitting, standing으로 이루어져 있습니다.  
하지만 우리는 lying과 sitting data만 이용해 사람을 detection 후 classification 하겠습니다.

### Thesis
Human Detection : [https://www.youtube.com/watch?v=WgsZc_wS2qQ&t=632s](https://www.youtube.com/watch?v=WgsZc_wS2qQ&t=632s)  
Human Segementation : [https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)

### Code
Human Detection은 4기 선배님이신 [유동근 선배님 코드](https://github.com/DonggeunYu/HumanDetectionCCTV)과 [빵형의 개발도상국님 코드](https://www.youtube.com/watch?v=WgsZc_wS2qQ)를 사용하였습니다.  
Model : [https://pytorch.org/vision/stable/models.html](https://pytorch.org/vision/stable/models.html)

## Sound
[잠박사 유튜브](https://www.youtube.com/channel/UClrKpnEehrQydacUHBptWcw/videos)

