import os
import numpy as np
import random
data_dir = 'D:\\Submission\\Testing-dataset\\test_data'
folder_clustermaps = 'D:\\data\\1-10\\cluster_maps_5'

list_image = os.listdir(data_dir)

for image in list_image:
    image_index = int(image[12:16])
    path_image = os.path.join(data_dir, image)
    cluster_map = os.path.join(folder_clustermaps, image[:16] + '.npy')
    cluster_map = np.load(cluster_map)
    loc = []
    list_patch = os.listdir(path_image)
    for patch in list_patch:
        path_patch = os.path.join(path_image, patch)
        h = int(patch[17:20])
        w = int(patch[21:24])
        if cluster_map[h][w] != 2:
            os.remove(path_patch)

    list_patch = os.listdir(path_image)
    random.shuffle(list_patch)
    for patch in list_patch[: int(0.8*len(list_patch))]:
        path_patch = os.path.join(path_image, patch)
        os.remove(path_patch)