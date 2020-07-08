# A neural network which approximates a logical operation (AND, OR, XOR, NAND).
# The shape of the network is hardcoded: one hidden and one output layer (the input
# layer does not count as a layer). Configuration of the layers is done via weight
# arrays W1 and W2. The number of nodes is defined using variables n_input_nodes,
# n_hidden_nodes and n_output_nodes.
#
# The example shows that the code of forward() and train() does not need to change
# when the number of nodes changes (as long as the number of layers remains the same).

import matplotlib.pyplot as plt
import numpy as np

import dataset
from activation import sigmoid

np.set_printoptions(formatter={"float": "{: 0.3f}".format}, linewidth=np.inf)
np.random.seed(1)

type = "xor_3_input"  # choose "xor_2_input" or "xor_3_input"

if type == "xor_2_input":
    X, Y = dataset.xor_2_input()
    n_input_nodes = 2
    n_hidden_nodes = 2
    n_output_nodes = 1
else:  # type == "xor_3_input":
    X, Y = dataset.xor_3_input()
    n_input_nodes = 3
    n_hidden_nodes = 3
    n_output_nodes = 1

W1 = np.random.normal(size=(n_hidden_nodes, n_input_nodes))  # layer 1 weights
W2 = np.random.normal(size=(n_output_nodes, n_hidden_nodes))  # layer 2 weights

B1 = np.random.random(size=(n_hidden_nodes, 1))  # layer 1 bias
B2 = np.random.random(size=(n_output_nodes, 1))  # layer 2 bias


def forward(x, predict=True):
    a0 = x.T
    z1 = W1.dot(a0) + B1
    a1 = sigmoid(z1)
    z2 = W2.dot(a1) + B2
    a2 = sigmoid(z2)
    if predict is False:
        return a0, z1, a1, z2, a2
    return a2


def train(x, y, iterations=10000, learning_rate=0.1):
    global W1, W2, B1, B2, error
    m = x.shape[0]
    error = []

    for _ in range(iterations):
        a0, z1, a1, z2, a2 = forward(x, predict=False)

        da2 = a2 - y.T
        dz2 = da2 * sigmoid(z2, derivative=True)
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

        error.append(np.average(da2 ** 2))

    return error


error = train(X, Y, iterations=50000, learning_rate=0.2)

plt.plot(error)
plt.xlabel("training iterations")
plt.ylabel("mse")

Y_hat = forward(X)

print("predict:", Y_hat)
print("desired:", Y.T)
print("error  :", Y.T - Y_hat)

plt.show()
