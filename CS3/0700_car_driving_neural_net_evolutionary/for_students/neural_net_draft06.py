'''
https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
http://neuralnetworksanddeeplearning.com/chap1.html
https://medium.com/learning-new-stuff/how-to-learn-neural-networks-758b78f2736e

Backprop best:
https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/

What should weights and biases start out at?
'''
import math, random

def mse(array):
    '''Mean squared error function that calculates
    mean squared error for an arbitrary target.

    There are many ways to calculate error.
    The square in this error calculation exaggerates
    the error.'''
    sse = 0 #sum of squares error
    for i in range(len(array)):
        sse += (target_outputs[i]-array[i])**2
    return sse/len(array)

def backpropagate(nn, eta, target_outputs):
    '''eta is the learning rate.
    nn is a neural net object'''
    #Loop over output layer indicies
    for i in range(len(nn.layers[-1])):
        #Get an output neuron
        out_neuron=nn.layers[-1][i]
        #Get the corresponding target value
        target=target_outputs[i]
        #Calculate derivative of error with respect to output i
        derror_douti = (2/len(target_outputs))*(target-out_neuron.out)
        #Backpropogate
        out_neuron.backpropagate(derror_douti)


def sigmoid(z):
    '''This is an S-shaped function.
    The sum of the weighted inputs to each neuron
    are fed through a sigmoid function.'''
    return 1/(1+math.exp(-z))

def forwardPropagate(layer1, layer2):
    '''layer1 and layer2 are lists of neurons.
    layer2 is further forward in the network.

    This function feeds weighted input from layer1
    into layer2 and calulates layer2's neurons'
    outputs.'''
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
            temp += layer1[j].out*h.weights[j]
        #Record the net input from the previous layer
        #for neuron i in the variable net_in.
        #This is useful for calculating te backpropagation.
        h.net_in = temp
        #The output of neuron i
        h.out = sigmoid(temp)


class Neuron:
    def __init__(self, input_neurons):
        '''input_neurons is a list of the neurons
        that input to this neuron. There WILL be a dummy
        layer of neurons on the front end that themselves
        have no input.'''
        self.out = 0 #output of this neuron
        self.bias = 0 #random.random()*2-1 #TODO: what is bias and how do I initialize it?
        #Keep track of sum of weighted inputs
        #(aka net input) purely for calculating
        #backprop derivative.
        self.net_in = None
        #Construct list of weights randomized
        #between -1 and 1.
        self.weights = []
        for _ in range(len(input_neurons)):
            self.weights.append(random.random()*2-1)
        #Remember input neurons for backprop
        self.inputs = input_neurons

    def backpropagate(self, derror_dout):
        #Base case
        if len(self.inputs)==0:
            return
        #Calculate derivative of output with respect to net_input
        dout_dinput = -(sigmoid(self.net_in)**2)*(math.exp(-self.net_in))
        #Loop over inputs to learn and to backpropagate recursively
        for i in range(len(self.inputs)):
            #update the weight of the output neuron
            derror_dweight = derror_dout * dout_dinput * self.inputs[i].out
            #Learn
            self.weights[i] -= derror_dweight * eta
            #Backprop recursively
            self.inputs[i].backpropagate(derror_dweight)

    def getCopy(self):
        '''Return a deep copy of this neuron.'''
        n = Neuron(self.inputs)
        n.out = self.out
        n.bias = self.bias
        n.net_in = self.net_in
        n.weights = []
        for w in self.weights:
            n.weights.append(w)
        return n


class NeuralNet:
    def __init__(self, layers):
        '''layers is an array of integers signifying
        the number of neurons per layer.

        if layers contains [3,6,2] this means that the first
        layer of 3 neurons are dummy neurons used purely for input.
        The next 6 neurons have 3 inputs. The next (output)
        layer has 2 neurons.
        This is the arrangement since the weights precede every
        neuron.'''
        self.layers = []
        #Add in dummy layer
        temp = []
        for _ in range(layers[0]):
            temp.append(Neuron([]))
        self.layers.append(temp)
        #Add in all the real layers
        for i in range(1,len(layers)):
            temp = []
            for _ in range(layers[i]):
                temp.append(Neuron(self.layers[i-1]))
            self.layers.append(temp)

    def getCopy(self):
        '''Return a deep copy of this neural net.'''
        copy = NeuralNet([0])
        copy.layers = []
        for layer in self.layers:
            temp = []
            for neuron in layer:
                n = neuron.getCopy()
                temp.append(n)
                if len(copy.layers) > 0:
                    n.inputs = copy.layers[-1]
            copy.layers.append(temp)
        return copy


    def predict(self, inputs):
        '''Perform a pass of forward propagation.'''
        #Put the inputs in the dummy layer
        for i in range(len(inputs)):
            self.layers[0][i].out = inputs[i]
        #Forward propagate
        for i in range(len(self.layers)-1):
            forwardPropagate(self.layers[i], self.layers[i+1])

    def getOutputs(self):
        '''Return a list of numeric output values.'''
        array = []
        for o in self.layers[-1]:
            array.append(o.out)
        return array

    def printOutputs(self):
        print(self.getOutputs())

    def sameAs(self, other):
        '''Other is a neural net. This function returns True
        if self and other have the same layers, number of
        neurons, and the same weights on those neurons.
        Originally this was created to verify that mutation
        and getCopy are working.'''
        if len(self.layers) != len(other.layers):
            return False
        for i in range(len(self.layers)):
            if len(self.layers[i]) != len(other.layers[i]):
                return False
            for j in range(len(self.layers[i])):
                neuron1 = self.layers[i][j]
                neuron2 = other.layers[i][j]
                if len(neuron1.weights) != len(neuron2.weights):
                    return False
                for k in range(len(neuron1.weights)):
                    if neuron1.weights[k] != neuron2.weights[k]:
                        return False
        return True

    def verifyInputLayer(self):
        '''This function compares the weights of neurons in the
        input layer by accessing the first layer directly in the
        array and separately accessing the first layer by
        pathing through neuron inputs.
        It's important to verify that the results are the same
        because of the complexity of the getCopy function.'''
        #Get first neuron in the output layer
        n = self.layers[-1][0]
        #Tunnel back to the input layer
        while len(n.inputs[0].inputs) > 0:
            n = n.inputs[0]
        #Verify same length
        if len(n.inputs) != len(self.layers[0]):
            print('ERROR in verifyInputLayer: length mismatch'); exit()
        #Change an input weight to see if the change is reflected
        #in both references.
        n.inputs[0].weights.append(783) #arbitrary number
        if self.layers[0][0].weights[-1] != 783:
            print('ERROR in verifyInputLayer: reference mismatch'); exit()
        #Reset the weight
        n.inputs[0].weights.pop(len(n.inputs[0].weights)-1)



if __name__ == "__main__":
    #Arbitrary goal outputs for testing purposes:
    target_outputs = [0.8,0.8,0.8,0.2,0.2,0.2,0.2,0.2,0.2]

    layer_neuron_counts = [9,6,9]
    my_nn = NeuralNet(layer_neuron_counts)
    eta = 0.8
    inputs = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
    for i in range(100): #Do 100 learning iterations
        my_nn.predict(inputs)
        my_nn.printOutputs()
        outputs = my_nn.getOutputs()
        total_error = mse(outputs)
        print('Error: '+str(total_error))
        #Learn
        backpropagate(my_nn, eta, target_outputs)
