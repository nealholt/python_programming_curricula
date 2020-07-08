# Two layer neural network capable of processing multiple inputs in one pass. Pre-defined weights and biases.
# Shape definition is done via the weight arrays W1, W2. Bias is not separate but included as an additional weight.
# Is able to recognize if an image contains a vertical bar or not.


import numpy as np

import dataset

W1 = np.array([[+1, -2, +1, -2, -1], [-2, +1, -2, +1, -1]])  # layer 1: 2 nodes with 4 inputs per node + bias input
W2 = np.array([[+1, +1, 0]])  # layer 2: 1 node with 2 inputs + bias input

X, Y = dataset.image2x2_set(no_of_sets=1, vertical_only=True)

a = X.T

for w in [W1, W2]:
    z = w.dot(np.vstack([a, np.ones([1, a.shape[1]])]))  # add the bias input which is always 1
    a = np.where(z > 0, 1, 0)  # step activation

print("predict:", a)
print("desired:", Y.T)
print("error  :", (Y.T - a))
