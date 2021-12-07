import numpy as np

def color_masks(image, classes='default'):
    colors = [[20, 20, 20], [255, 255, 255]]
    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)

    if classes == 'human':
        r[image == 1], g[image == 1], b[image == 1] = colors[1]
        colored_mask = np.stack([r, g, b], axis=2)
        return colored_mask
    else:
        r[image == 1], g[image == 1], b[image == 1] = colors[0]
        colored_mask = np.stack([r, g, b], axis=2)
        return colored_mask