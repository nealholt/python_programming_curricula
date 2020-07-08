# activation functions for usage in a neural network

import numpy as np


def sigmoid(z, derivative=False):
    if derivative:
        z = sigmoid(z)
        return z * (1 - z)
    z = np.clip(z, -500, 500)  # avoid overflow
    return 1 / (1 + np.exp(-z))


def linear(z, derivative=False):
    if derivative:
        return np.ones(z.shape)
    return z


def gaussian(z, derivative=False):
    if derivative:
        return -2 * z * np.exp(-z ** 2)
    return np.exp(-z ** 2)


def tanh(z, derivative=False):
    if derivative:
        return 1.0 - np.tanh(z) ** 2
    return np.tanh(z)


def relu(z, derivative=False):
    if derivative:
        np.greater(z, 0)
    return np.maximum(0, z)


def softplus(z, derivative=False):
    # A ReLU alternative which is really differentiable
    if derivative:
        z = softplus(z)
        return z * (1 - z)
    return np.log(1.0 + np.exp(-abs(z))) + max(z, 0)  # variant on np.log(1.0 + np.exp(z)) which cannot overflow
