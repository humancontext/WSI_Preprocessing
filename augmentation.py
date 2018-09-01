import os
from skimage import io
import numpy as np
import pandas as pd
import utils

N_AUG_TRAN = 8
N_AUG_COLOR = 8
INPUT_FOLDER = 'D:\\data\\1-10\\10_png_tiles_norm'
OUTPUT = 'D:\\data\\1-10\\10_png_tiles_aug'
CSV_PATH = 'D:\\data\\1-10\\data.csv'
dict_datatype = {}
dict_5yrs = {}
df = pd.read_csv(CSV_PATH)

# unevnely augment the normalized patches
if __name__ == '__main__':
    for i in range(len(df)):
        dict_5yrs[df.loc[i]['ImageIndex']] = df.loc[i]['5yrs']
        dict_datatype[df.loc[i]['ImageIndex']] = df.loc[i]['data_type']
    list_folders = os.listdir(INPUT_FOLDER)
    for folder in list_folders[1:]:
        image_index = int(folder[12:16])
        if dict_datatype[image_index] == 'train' and dict_5yrs[image_index] == 1:
            index = 1
            path_folder = os.path.join(INPUT_FOLDER, folder)
            list_tiles = os.listdir(path_folder)
            for tile in list_tiles:
                print('Folder: %s: finished %.2f%% ' % (folder, index/len(list_tiles)*100), end='\r', flush=True)
                index += 1
                tile_name = tile[:-4]
                path_tile = os.path.join(path_folder, tile)
                img = io.imread(path_tile)
                img = np.asarray(img, dtype='uint8')
                if dict_5yrs[image_index] == 1:
                    augmented = utils.augment_transformation(img, 4)
                else:
                    augmented = [img]
                augmented = augmented[1:]
                augmented = utils.augmentor_color(augmented)
                augmented = utils.augmentor_blur(augmented)
                for i in range(len(augmented)):
                    j = i + 1
                    output_folder = os.path.join(OUTPUT, folder+'_'+str(i+6))
                    if not os.path.isdir(output_folder):
                        os.mkdir(output_folder)
                    tile_name_aug = tile_name + '_' + str(i + 6) + '.png'
                    output_path = os.path.join(output_folder, tile_name_aug)
                    io.imsave(output_path, augmented[i])