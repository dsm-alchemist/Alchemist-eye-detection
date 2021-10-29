# Alchemist-timer-stop-condition

Alchemist 서비스 중 하나인 타이머를 자동으로 멈춰주는 기능입니다.

5분에 한번씩 5초 동안 5장의 사진을 찍어 첫번째로 사람을 detect 합니다. 만약 사람이 없다면 타이머를 멈춥니다.

두번째로 사람이 지금 누워있는지 일어나있는지 classification을 통해 누워있다면 타이머를 멈춥니다.

## Installation

Please check Installation procedure in [Install.md](https://github.com/CV-JaeHa/virtual-environment-list/blob/main/torchcv.md)



## Reference

### Data

Please download datas follow this [link](https://www.kaggle.com/deepshah16/silhouettes-of-human-posture?select=bending).

data label은 bending, lying, sitting, standing으로 이루어져 있습니다.

하지만 우리는 lying과 sitting data만 이용해 사람을 detect후 classiification 하겠습니다.



## Sound

[잠박사 유튜브](https://www.youtube.com/channel/UClrKpnEehrQydacUHBptWcw/videos)

