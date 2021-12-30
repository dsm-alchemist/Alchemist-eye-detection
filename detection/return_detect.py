# Import Library
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def return_detect(model, img, input_img, THRESHOLD=0.5):
    try:
        # Inference
        out = model([input_img])[0]
        for box, score in zip(out['boxes'], out['scores']):
            score = score.detach().numpy()

            # 사람일 확률
            return score > THRESHOLD
    # TODO: Set Exception Class
    except:
        return False
    """
    # Visualization 코드입니다. Try구문에 return True 대신 pass를 넣어주세요
    else:
        for box, score in zip(out['boxes'], out['scores']):
            score = score.detach().numpy()

            # 사람일 확률
            if score > THRESHOLD:
                fig, ax = plt.subplots(1, figsize=(16, 16))
                # box 좌표
                # box 0 : x1
                # box 1 : y1
                # box 2 : x2
                # box 3 : y2
                box = box.detach().numpy()

                rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='b',
                                         facecolor='none')
                ax.add_patch(rect)
                ax.imshow(img)
                plt.show()
                return True
            else:
                return False
    """