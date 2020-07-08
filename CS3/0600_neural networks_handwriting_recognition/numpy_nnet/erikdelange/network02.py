# Fully configurable neural network in numpy
#
# Usage: NN(shape_tuple, activation_tuple)
# shape_tuple: (nodes_in_input_layer, nodes_in_hidden_layer_1, ..., nodes_in_output_layer)
# activation_tuple: (None, activation_function_for_hidden_layer_1, ..., activation_function_for_output_layer)

import matplotlib.pyplot as plt
import numpy as np

import dataset
from activation import sigmoid

np.set_printoptions(formatter={"float": "{: 0.3f}".format}, linewidth=np.inf)
np.random.seed(1)


class NN:
    def __init__(self, shape, activation=None):
        self.num_layers = len(shape) - 1  # the input layer does not count as a layer
        self.weight = []
        self.bias = []

        if activation is None:  # activation tuple is optional
            self.activation = [sigmoid for _ in range(self.num_layers)]
        else:
            if len(shape) != len(activation):
                raise ValueError("nr of layers ({}) must match activations ({})".format(len(shape), len(activation)))
            self.activation = activation[1:]  # skip the activation function for the input layer

        self.a = []  # layers output after activation, input to the next layer
        self.z = []  # layers results before activation
        self.dw = []  # empty array used for weight update during training
        self.db = []  # empty array used for bias update during training

        for (layer1, layer2) in zip(shape[:-1], shape[1:]):
            self.weight.append(np.random.normal(size=(layer2, layer1)))
            self.bias.append(np.random.normal(size=(layer2, 1)))
            self.dw.append(np.zeros((layer2, layer1)))
            self.db.append(np.zeros((layer2, 1)))

    def forward(self, x):
        self.a = [x.T]  # a[0] is the input for layer 1 (layer 0 is the input layer)
        self.z = [None]

        for (weight, bias, activation) in zip(self.weight, self.bias, self.activation):
            self.z.append(weight.dot(self.a[-1]) + bias)
            self.a.append(activation(self.z[-1]))

        return self.a[-1].T

    def back_propagation(self, x, y, learning_rate=0.1, momentum=0.5):
        m = x.shape[0]
        delta_w = []
        delta_b = []

        y_hat = self.forward(x)

        e_y_hat = []
        for a in range(len(y_hat)):
            place = 0
            max_val = 0
            for b in range(len(y_hat[a])):
                if y_hat[a][b] > max_val:
                    place = b
                    max_val = y_hat[a][b]

            e_y_hat.append(place)

        y_hat = e_y_hat

        error = np.sum((y_hat - y) ** 2)

        for index in reversed(range(1, self.num_layers + 1)):
            if index == self.num_layers:
                da = self.a[index] - y.T
            else:
                da = self.weight[index].T.dot(dz)
            dz = da * self.activation[index - 1](self.z[index], derivative=True)
            dw = dz.dot(self.a[index - 1].T) / m
            db = np.sum(dz, axis=1, keepdims=True) / m

            delta_w.append(dw)
            delta_b.append(db)

        for (index, dw, db) in zip(reversed(range(self.num_layers)), delta_w, delta_b):
            self.dw[index] = learning_rate * dw + momentum * self.dw[index]
            self.weight[index] -= self.dw[index]
            self.db[index] = learning_rate * db + momentum * self.db[index]
            self.bias[index] -= self.db[index]

        return error

    def train(self, x, y, iterations=10000, learning_rate=0.2, momentum=0.5, verbose=True):
        min_error = 1e-5
        loss = []

        for i in range(iterations + 1):
            error = self.back_propagation(x, y, learning_rate=learning_rate, momentum=momentum)
            loss.append(error)
            if verbose:
                if i % 2500 == 0:
                    print("iteration {:5d} error: {:0.6f}".format(i, error))
                if error <= min_error:
                    print("minimum error {} reached at iteration {}".format(min_error, i))
                    break

        return loss




'''Source of the neural network is here:
https://github.com/erikdelange/Neural-networks-in-numpy
I have not verified that the numpy data I'm loading in is
properly formatted. Printing it out in some way is the next
thing to do.

I'm hoping I can iteratively train the neural network on
chunks of the handwriting data.
'''
input_count = 785
line_count = 42000
training_percent = 0.5 #Train on this percent of data
row_count = 100 #Train on this many rows at a time
data=np.loadtxt('../../data/train.csv',skiprows=1,delimiter=",",
                usecols=range(1,input_count), max_rows=row_count)
targets=np.loadtxt('../../data/train.csv',skiprows=1,delimiter=",",
                usecols = 0, max_rows=row_count)

network = NN((784, 50, 10), (None, sigmoid, sigmoid))

error = network.train(data, targets, 5000, learning_rate=0.2)

plt.plot(error)
plt.xlabel("training iterations")
plt.ylabel("mse")

Y_hat = network.forward(data)

'''Previously there was an error because Y_hat had
shape 100x10, but should have had shape 100x1.
I forgot to take the ten outputs of the neural net
and only use the highest "voted" index as the
chosen value for the handwritten digit. The
following code fixes that mistake.'''
e_y_hat = [] #e for edited
for a in range(len(Y_hat)):
    place = 0
    max_val = 0
    for b in range(len(Y_hat[a])):
        if Y_hat[a][b] > max_val:
            place = b
            max_val = Y_hat[a][b]

    e_y_hat.append(place)

Y_hat = e_y_hat

print("predict:", Y_hat.T)
print("desired:", targets.T)
print("loss   :", (targets - Y_hat).T)

plt.show()
