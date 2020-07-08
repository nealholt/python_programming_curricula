# A neural network which approximates linear function y = 2x + 3.
# The network has 1 layer with 1 node, which has 1 input (and a bias).
# As there is no activation effectively this node is a linear function.
# After +/- 10.000 iterations W should be close to 2 and B should be close to 3.

import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(formatter={"float": "{: 0.3f}".format}, linewidth=np.inf)
np.random.seed(1)

X = np.array([[0], [1], [2], [3], [4]])  # X = input (here: 5 values)
Y = 2 * X + 3  # Y = output: y = 2x + 3 (as many values as there are X's)

W = np.random.normal(scale=0.1, size=(1, 1))  # layer: (1, 1) = 1 node with 1 input
B = np.random.normal(scale=0.1, size=(1, 1))  # bias: (1, 1) = for 1 node (and by definition only 1 bias value per node)

learning_rate = 0.001
iterations = 10000
error = []

print("initial :", "W =", W, "B =", B, "(random initialization)")

m = X.shape[0]

for _ in range(iterations):
    # forward pass
    a = W.dot(X.T) + B

    # back propagation
    da = a - Y.T  # da = error
    dz = da  # no activation
    dw = dz.dot(X) / m
    db = np.sum(dz, axis=1, keepdims=True) / m

    W -= learning_rate * dw
    B -= learning_rate * db

    error.append(np.average(da ** 2))

print("result  :", "W =", W, "B =", B, "(after {} iterations)".format(iterations))
print("expected: W = 2, B = 3")

plt.plot(range(iterations), error)
plt.title("MSE (mean squared error)")
plt.xlabel("training iterations")
plt.ylabel("mse")
plt.show()
