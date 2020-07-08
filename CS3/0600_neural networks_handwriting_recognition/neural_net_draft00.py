#tic tac toe
'''
https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
http://neuralnetworksanddeeplearning.com/chap1.html
https://medium.com/learning-new-stuff/how-to-learn-neural-networks-758b78f2736e

START HERE Backprop best:
https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/

Loss functions and then backprop are the next steps?
What should weights and biases start out at?
'''
import math, random

NUM_INPUTS = 9

def score(array):
    '''Dummy function that gives perfect score if
    first 3 outputs are 1 and last three are 0.'''
    sse = 0 #sum of squares error
    for i in array[:3]:
        sse += (i-0.8)**2
    for i in array[3:]:
        sse += (i-0.2)**2
    return sse


def sigmoid(z):
    return 1/(1+math.exp(-z))

def predictHelper(layer1, layer2):
    #loop through next layer
    for i in range(len(layer2)):
        #Get current neuron to update
        h = layer2[i]
        #Start with the neuron's bias
        temp = h.bias
        #Loop through previous layer, adding
        #weight * neuron output to our temp
        #variable
        for j in range(len(layer1)):
            temp += layer1[j].value*h.weights[j]
        h.value = sigmoid(temp)


class Neuron:
    def __init__(self, num_inputs):
        self.value = 0
        self.weights = []
        self.bias = random.random()*2-1
        for _ in range(num_inputs):
            self.weights.append(random.random()*2-1)


class NeuralNet:
    def __init__(self):
        self.input_layer = []
        self.hidden_layer = []
        self.output_layer = []
        for _ in range(NUM_INPUTS):
            self.input_layer.append(Neuron(NUM_INPUTS))
            self.hidden_layer.append(Neuron(NUM_INPUTS))
            self.output_layer.append(Neuron(NUM_INPUTS))

    def reset(self):
        for i in range(NUM_INPUTS):
            self.input_layer[i].value = 0
            self.hidden_layer[i].value = 0
            self.output_layer[i].value = 0

    def predict(self):
        #input layer feeds into hidden layer
        predictHelper(self.input_layer, self.hidden_layer)
        #hidden layer feeds into output layer
        predictHelper(self.hidden_layer, self.output_layer)

    def getOutputs(self):
        array = []
        for o in self.output_layer:
            array.append(o.value)
        return array

    def printOutputs(self):
        print(self.getOutputs())


my_nn = NeuralNet()
my_nn.predict()
my_nn.printOutputs()
total_error = my_nn.getOutputs()
print(score(total_error))