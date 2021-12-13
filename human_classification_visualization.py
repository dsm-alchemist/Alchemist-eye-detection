# Import Library
from __future__ import print_function, division
import torch
import matplotlib.pyplot as plt
from human_classification_hyperparameter import dataloaders, class_names

def visualize_model(model, num_images=6):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    was_training = model.training
    model.eval()
    images_so_far = 0
    fig = plt.figure()

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders['test']):
            inputs = inputs.to(device)
            labels = inputs.to(device)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            for j in range(inputs.size()[0]):
                images_so_far += 1
                ax = plt.subplots(num_images // 2, 2, images_so_far)
                ax.axis('off')
                ax.set_title(f'predicted : {class_names[preds[j]]}')
                plt.imshow(inputs.cpu().data[j])

                if images_so_far == num_images:
                    model.train(mode=was_training)
                    return
        model.train(model=was_training)