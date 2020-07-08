# Third degree polynomial solved by a neural network

import matplotlib.pyplot as plt
import numpy as np

from activation import sigmoid, linear

np.set_printoptions(formatter={"float": "{: 0.3f}".format}, linewidth=np.inf)
np.random.seed(1)

x = np.linspace(-5, +5, 1000)
y = x ** 3 - 15 * x

X = x.reshape(-1, 1)  # from [x] to [1][x]
Y = y.reshape(-1, 1)

n_input_nodes = 1
n_hidden_nodes = 8  # the higher the number of nodes the better the fit (e.g. try values from 2 to 10)
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
    a2 = linear(z2)
    if predict is False:
        return a0, z1, a1, z2, a2
    return a2


def train(x, y, iterations=50000, learning_rate=0.001):
    global W1, W2, B1, B2, error
    m = x.shape[0]
    error = []

    for _ in range(iterations):
        a0, z1, a1, z2, a2 = forward(x, predict=False)

        da2 = a2 - y.T
        dz2 = da2 * linear(z2, derivative=True)
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


error = train(X, Y, iterations=10000, learning_rate=0.002)  # lower learning rates give a better fit

plt.plot(error)
plt.title("MSE (mean squared error)")
plt.xlabel("training iterations")
plt.ylabel("mse")
plt.show()

Y_hat = forward(X)

plt.plot(x, y, label=r"function: $x^3 - 15x$")
plt.plot(x, Y_hat.T, label="prediction ({} nodes)".format(n_hidden_nodes))
plt.legend()
plt.show()
