# Import Library
import matplotlib.pyplot as plt
import matplotlib.patches as patchess

def return_detect(model, input_img, THRESHOLD):
    try:
        # Inference
        out = model([input_img])[0]
        # print(out.keys())
        """
        dict_keys(['boxes', 'labels', 'scores', 'keypoints', 'keypoints_scores'])
        우리는 boxes score를 사용하겠다.
        """
    except:
        return False
    else:
        # fig, ax = plt.subplots(1, figsize=(16, 16))

        for box, score in zip(out['boxes'], out['scores']):
            score = score.detach().numpy()

            # 사람일 확률
            if score < THRESHOLD:
                continue

            """ box 좌표
            box 0 : x1
            box 1 : y1
            box 2 : x2
            box 3 : y2 """
            # box = box.detach().numpy()

            """ 사람 그리기
            rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='b', facecolor='none')
            ax.add_patch(rect)
            ax.imshow(img)
            plt.show()
            """
            return True