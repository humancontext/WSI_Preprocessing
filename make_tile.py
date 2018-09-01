import os
from skimage import io
import numpy as np
# import png
from PIL import Image

# breaks the normalized WSI into 224x224 patches
def main():
    path = "D:\\data\\1-10\\10_png_norm\\"
    Image.MAX_IMAGE_PIXELS = 399231110
    files = os.listdir(path)
    index = 1
    for ii in [0]:
        png_file_1 = io.imread(path + files[ii], as_gray=False)
        png_file_2 = io.imread(path + files[ii + 1], as_gray=False)
        png_file_3 = io.imread(path + files[ii + 2], as_gray=False)
        png_file_4 = io.imread(path + files[ii + 3], as_gray=False)
        up = np.hstack((png_file_1, png_file_2))
        low = np.hstack((png_file_3, png_file_4))
        array = np.vstack((up, low))
        dimension = 224
        n_height = int(array.shape[0]/dimension)
        n_width = int(array.shape[1]/dimension)

        dir = 'D:\\data\\1-10\\10_png_tiles_norm\\' + files[ii][:16] + "\\"

        try:
            os.stat(dir)
        except:
            os.mkdir(dir)

        tile_index = 0
        total = n_height * n_width
        for i in range(n_height):
            for j in range(n_width):
                tile_index += 1
                tile = array[i*dimension:(i+1)*dimension, j*dimension:(j+1)*dimension]
                io.imsave(dir + files[ii][0:17] + str(i) + "_" + str(j) + ".png", tile)
                print('working with %d file(s) of %d files:  %.2f' % (index, len(files)/4, tile_index/total*100), end='\r', flush=True)
        index += 1


if __name__ == "__main__":
    main();