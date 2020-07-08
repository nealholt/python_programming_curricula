# Two layer neural network capable of processing multiple inputs in one pass. Pre-defined weights and biases.
# Shape definition is done via the weight arrays W1, W2. Bias is separate.
# Is able to recognize if an image contains a vertical bar or not.

import numpy as np

import dataset

W1 = np.array([[+1, -2, +1, -2], [-2, +1, -2, +1]])  # layer 1: 2 nodes with 4 inputs per node
W2 = np.array([[+1, +1]])  # layer 2: 1 node with 2 inputs + bias input
B1 = np.array([[-1], [-1]])  # bias for nodes in layer 1
B2 = np.array([[0]])  # bias for nodes in layer 2

X, Y = dataset.image2x2_set(no_of_sets=2, vertical_only=True)

a = X.T

for w, b in zip([W1, W2], [B1, B2]):
    z = w.dot(a) + b
    a = np.where(z > 0, 1, 0)  # step activation

print("predict:", a)
print("desired:", Y.T)
print("error  :", (Y.T - a))
