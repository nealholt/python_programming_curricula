# A trainable neural network for 2x2 image recognition.
# The network shape is hardcoded via the W1, W2, W3 arrays (i.e. 3 layers, not counting the inputs).
# Is able to recognize 4 different shapes in a 2x2 pixel image (see dataset.py for details on this).

import matplotlib.pyplot as plt
import numpy as np

import dataset
from activation import sigmoid

np.set_printoptions(formatter={"float": "{: 0.3f}".format}, linewidth=np.inf)
np.random.seed(1)

W1 = np.random.normal(size=(16, 4))  # layer 1 weights: 16 nodes with 4 inputs per node
W2 = np.random.normal(size=(8, 16))  # layer 2 weights: 8 nodes with 16 inputs per node
W3 = np.random.normal(size=(4, 8))  # layer 3 weights: 4 nodes with 8 inputs per node

B1 = np.random.random(size=(16, 1))  # layer 1 bias: 16 nodes (by definition each with 1 bias)
B2 = np.random.random(size=(8, 1))  # layer 2 bias: 8 nodes (by definition each with 1 bias)
B3 = np.random.random(size=(4, 1))  # layer 3 bias: 4 nodes (by definition each with 1 bias)


def forward(x, predict=True):
    a0 = x.T
    z1 = W1.dot(a0) + B1
    a1 = sigmoid(z1)
    z2 = W2.dot(a1) + B2
    a2 = sigmoid(z2)
    z3 = W3.dot(a2) + B3
    a3 = sigmoid(z3)

    if predict is False:
        return a0, z1, a1, z2, a2, z3, a3
    return a3


def train(x, y, iterations=10000, learning_rate=0.1):
    global W1, W2, W3, B1, B2, B3, error
    m = x.shape[0]
    error = []

    for _ in range(iterations):
        a0, z1, a1, z2, a2, z3, a3 = forward(x, predict=False)

        da3 = a3 - y.T
        dz3 = da3 * sigmoid(z3, derivative=True)
        dw3 = dz3.dot(a2.T) / m
        db3 = np.sum(dz3, axis=1, keepdims=True) / m

        da2 = W3.T.dot(dz3)
        dz2 = np.multiply(da2, sigmoid(z2, derivative=True))
        dw2 = dz2.dot(a1.T) / m
        db2 = np.sum(dz2, axis=1, keepdims=True) / m

        da1 = W2.T.dot(dz2)
        dz1 = np.multiply(da1, sigmoid(z1, derivative=True))
        dw1 = dz1.dot(a0.T) / m
        db1 = np.sum(dz1, axis=1, keepdims=True) / m

        W1 -= learning_rate * dw1
        B1 -= learning_rate * db1
        W2 -= learning_rate * dw2
        B2 -= learning_rate * db2
        W3 -= learning_rate * dw3
        B3 -= learning_rate * db3

        error.append(np.average(da2 ** 2))

    return error


X, Y = dataset.image2x2_set()

error = train(X, Y, iterations=50000, learning_rate=0.2)

plt.plot(error)
plt.xlabel("training iterations")
plt.ylabel("mse")

Y_hat = forward(X)

print("predict:", Y_hat)
print("desired:", Y.T)
print("error  :", Y.T - Y_hat)

plt.show()
