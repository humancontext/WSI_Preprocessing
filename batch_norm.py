from staintools import ReinhardColorNormalizer
import os
from skimage import io
import png
from PIL import Image

Image.MAX_IMAGE_PIXELS = 3176832150


# the reinhard image normalization is implemented to normalize the WSI in 2x2 batches.
def main():
    input_path = "D:\\data\\1-10\\10_png\\"
    input_folders = os.listdir(input_path)
    n = ReinhardColorNormalizer()
    standard = io.imread('D:\\data\\1-10\\10_png\\2018_04_05__4820_ORG.png', as_gray=False)
    n.fit(standard)
    index = 1
    for image_name in input_folders[3:]:
        print('Folder: %s: finished %d of %d (00%%) ' % (image_name, index, len(input_folders) - 1), end='\r', flush=True)
        index += 1
        file_path = input_path + image_name
        output_path = 'D:\\data\\1-10\\4\\'
        try:
            os.stat(output_path)
        except:
            os.mkdir(output_path)
        image = io.imread(file_path, as_gray=False)
        len_half1 = int(len(image)/2)
        len_half2 = int(len(image[0])/2)
        image1 = image[:len_half1, :len_half2, :]
        image2 = image[:len_half1, len_half2:, :]
        image3 = image[len_half1:, :len_half2, :]
        image4 = image[len_half1:, len_half2:, :]

        norm_image1 = n.transform(image1)
        png.from_array(norm_image1, 'RGB').save(output_path + image_name[:16] + '_1.png')
        print('Folder: %s: finished %d of %d (25%%) ' % (image_name, index, len(input_folders) - 1), end='\r', flush=True)

        norm_image2 = n.transform(image2)
        png.from_array(norm_image2, 'RGB').save(output_path + image_name[:16] + '_2.png')
        print('Folder: %s: finished %d of %d (50%%) ' % (image_name, index, len(input_folders) - 1), end='\r', flush=True)

        norm_image3 = n.transform(image3)
        png.from_array(norm_image3, 'RGB').save(output_path + image_name[:16] + '_3.png')
        print('Folder: %s: finished %d of %d (75%%) ' % (image_name, index, len(input_folders) - 1), end='\r', flush=True)

        norm_image4 = n.transform(image4)
        png.from_array(norm_image4, 'RGB').save(output_path + image_name[:16] + '_4.png')


if __name__ == "__main__":
    main();
