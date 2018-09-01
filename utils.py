from skimage import io
import numpy as np
from imgaug import augmenters as iaa


def augmentor_color(images):
    for i in range(len(images)):
        images.append(iaa.Multiply(0.75).augment_image(images[i]))
        images.append(iaa.Multiply(1.25).augment_image(images[i]))
    return images


def augmentor_blur(images):
    for i in range(len(images)):
        images.append(iaa.GaussianBlur(sigma=1).augment_image(images[i]))
    return images


def augment_transformation(input, n):
    images = []
    if n > 0:
        images.append(input)
    if n > 1:
        images.append(np.flipud(input))
    if n > 2:
        images.append(np.fliplr(input))
    if n > 3:
        images.append(np.rot90(input))
    if n > 4:
        images.append(np.rot90(input, k=2))
    if n > 5:
        images.append(np.rot90(input, k=3))
    if n > 6:
        images.append(np.rot90(np.flipud(input)))
    if n > 7:
        images.append(np.rot90(np.flipud(input), k=3))
    return images