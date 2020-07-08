# example datasets which can be used in training and evaluating a neural network

import numpy as np


def xor_2_input():
    """ Truth table for a XOR operation with 2 inputs. """
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])  # input

    Y = np.array([[0.],
                  [1.],
                  [1.],
                  [0.]])  # output (true if odd number of inputs is true)

    return X, Y


def xor_3_input():
    """ Truth table for a XOR operation with 3 inputs. """
    X = np.array([[0, 0, 0],
                  [0, 0, 1],
                  [0, 1, 0],
                  [0, 1, 1],
                  [1, 0, 0],
                  [1, 0, 1],
                  [1, 1, 0],
                  [1, 1, 1]])  # input

    Y = np.array([[0.],
                  [1.],
                  [1.],
                  [0.],
                  [1.],
                  [0.],
                  [0.],
                  [1.]])  # output (true if odd number of inputs is true)

    return X, Y


def image2x2(vertical_only=False):
    """ Flattened 2 x 2 pixel images, each stored as 1D array of 4 long.
        Index of pixel in array: 0 | 1
                                 -----
                                 2 | 3
    """
    X = np.array([
        [0, 0, 0, 0],  # solid white
        [1, 1, 1, 1],  # solid black
        [1, 1, 0, 0],  # horizontal line, top
        [0, 0, 1, 1],  # horizontal line, bottom
        [1, 0, 1, 0],  # vertical line, left
        [0, 1, 0, 1],  # vertical line, right
        [1, 0, 0, 1],  # diagonal line, top-left bottom-right
        [0, 1, 1, 0],  # diagonal line, bottom-left top-right
        [1, 0, 0, 0],  # unknown shape
        [0, 1, 0, 0],  # unknown shape
        [0, 0, 1, 0],  # unknown shape
        [0, 0, 0, 1],  # unknown shape
        [1, 1, 0, 1],  # unknown shape
        [1, 1, 1, 0],  # unknown shape
        [0, 1, 1, 1],  # unknown shape
        [1, 0, 1, 1]  # unknown shape
    ])  # input: all possible image shapes (in black and white)

    Y = np.array([
        [1, 0, 0, 0],  # solid
        [1, 0, 0, 0],  # solid
        [0, 1, 0, 0],  # horizontal
        [0, 1, 0, 0],  # horizontal
        [0, 0, 1, 0],  # vertical
        [0, 0, 1, 0],  # vertical
        [0, 0, 0, 1],  # diagonal
        [0, 0, 0, 1],  # diagonal
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0],  # unknown shape
        [0, 0, 0, 0]  # unknown shape
    ])  # output: all possible labels (one-hot vector)

    Y_vertical_only = np.array([[0], [0], [0], [0], [1], [1], [0], [0],
                                [0], [0], [0], [0], [0], [0], [0], [0]])  # output: labels for vertical line only

    return X, Y if vertical_only is False else Y_vertical_only


def image2x2_set(no_of_sets=1, vertical_only=False):
    """ Return one or more sets of grayscale images. Every set contains all possible shapes (so 16 images). """
    grey_range = 0.2
    images = []
    labels = []

    img, lbl = image2x2(vertical_only=vertical_only)  # get the black and white images

    for _ in range(no_of_sets):  # convert to grayscale
        for (image, label) in zip(img, lbl):
            images.append([np.random.uniform(0.00, grey_range) if not p else np.random.uniform(1 - grey_range, 1.00)
                           for p in image])
            labels.append(label)

    return np.array(images), np.array(labels)
