# Alchemist-timer-stop-condition
Alchemist 서비스 중 하나인 타이머를 자동으로 멈춰주는 기능입니다.  
5분에 한번씩 5초 동안 5장의 사진을 찍어 첫번째로 사람을 detect 합니다. 만약 사람이 없다면 타이머를 멈춥니다.  
두번째로 사람이 지금 누워있는지 일어나있는지 classification을 통해 누워있다면 타이머를 멈춥니다.

## Installation
Please check Installation procedure in [Install.md](https://github.com/CV-JaeHa/virtual-environment-list/blob/main/torchcv.md)
```
# IF your device is mac os
% brew install libomp
% conda install flask
```

# 작동 알고리즘
1. server에서 5분마다 호출  
2. client에서 5초 동안 5장의 사진을 찍음  
3. client에서 찍은 사진은 server로 전송  
4. server에서 Resnet이 사람을 감지  
5. server에서 사람이 없다면 타이머 정지 (단 5개의 사진 모두 사람이 없어야 함)  
6. server에서 사람이 있다면 일어나있는지 누워있는지 분류모델을 실행  
7. 누워있다면 타이머 정지, 일어나 있다면 continue.

## Model
모델은 RMPE(Regional Multi-Person Pose Estimation)를 사용하였습니다.  
RMPE는 2step 방식을 사용합니다. 2step은 먼저 사람의 bounding box를 설정하고, 그 안에서 

## Reference

### Data
Please download datas follow this [posture link](https://www.kaggle.com/deepshah16/silhouettes-of-human-posture?select=bending), [sitting human link](http://www2.informatik.uni-freiburg.de/~oliveira/dataset.html).  
data label은 bending, lying, sitting, standing으로 이루어져 있습니다.  
하지만 우리는 lying과 sitting data만 이용해 사람을 detect후 classiification 하겠습니다.

### Thesis
Human Detection : [https://www.youtube.com/watch?v=WgsZc_wS2qQ&t=632s](https://www.youtube.com/watch?v=WgsZc_wS2qQ&t=632s)  
번역본 : [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=worb1605&logNo=221569880346](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=worb1605&logNo=221569880346)


### Code
Human Detection은 4기 선배님이신 [유동근 선배님 코드](https://github.com/DonggeunYu/HumanDetectionCCTV)를 사용하였습니다.  
Model : [https://github.com/MVIG-SJTU/RMPE](https://github.com/MVIG-SJTU/RMPE)

## Sound
[잠박사 유튜브](https://www.youtube.com/channel/UClrKpnEehrQydacUHBptWcw/videos)

