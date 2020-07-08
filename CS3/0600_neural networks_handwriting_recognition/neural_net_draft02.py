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

#This is not only number of inputs, but also number
#of neurons in the hidden layer and the output layer.
#Currently we are implementing a 3 layer neural net.
NUM_INPUTS = 9

#Arbitrary goal outputs for testing purposes:
target_outputs = [0.8,0.8,0.8,0.2,0.2,0.2,0.2,0.2,0.2]

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

def backpropagate(nn, eta):
    '''eta is the learning rate.'''
    #TODO: This is tested but complicated.
    for i in range(len(nn.output_layer)):
        out_neuron=nn.output_layer[i]
        target=target_outputs[i]
        #deriv of error with respect to output i
        derror_douti = (2/len(target_outputs))*(target-out_neuron.out)
        #deriv of output i with respect to net_input
        douti_dinput = -(sigmoid(out_neuron.net_in)**2)*(math.exp(-out_neuron.net_in))
        #loop over hidden layer
        for h in range(len(nn.hidden_layer)):
            #update the weight of the output neuron
            derror_dweight = derror_douti * douti_dinput * nn.hidden_layer[h].out
            out_neuron.weights[h] -= derror_dweight * eta
            #Backpropagate further

            #douth_dinput is the deriv of output i with respect
            #to net_input. This is not used, but it would be used
            #if we had another layer in our neural net.
            #douth_dinput = -(sigmoid(nn.hidden_layer[h].net_in)**2)*(math.exp(-nn.hidden_layer[h].net_in))

            for index in range(len(nn.input_layer)):
                #update the weight of the hidden neuron
                derror_dweight2 = derror_douti * douti_dinput * derror_dweight * nn.input_layer[index].out
                nn.hidden_layer[h].weights[index] -= derror_dweight2 * eta

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
    def __init__(self, num_inputs):
        self.out = 0 #output of this neuron
        self.bias = 0 #random.random()*2-1 #TODO: what is bias and how do I initialize it?
        #Keep track of sum of weighted inputs
        #(aka net input) purely for calculating
        #backprop derivative.
        self.net_in = None
        #Construct list of weights randomized
        #between -1 and 1.
        self.weights = []
        for _ in range(num_inputs):
            self.weights.append(random.random()*2-1)


class NeuralNet:
    def __init__(self):
        '''Create a 3-layer neural network.
        with 3xNUM_INPUTS neurons.'''
        self.input_layer = []
        self.hidden_layer = []
        self.output_layer = []
        for _ in range(NUM_INPUTS):
            self.input_layer.append(Neuron(NUM_INPUTS))
            self.hidden_layer.append(Neuron(NUM_INPUTS))
            self.output_layer.append(Neuron(NUM_INPUTS))

    def predict(self):
        '''Perform a pass of forward propagation.'''
        #input layer feeds into hidden layer
        forwardPropagate(self.input_layer, self.hidden_layer)
        #hidden layer feeds into output layer
        forwardPropagate(self.hidden_layer, self.output_layer)

    def getOutputs(self):
        '''Return a list of numeric output values.'''
        array = []
        for o in self.output_layer:
            array.append(o.out)
        return array

    def printOutputs(self):
        print(self.getOutputs())


my_nn = NeuralNet()
eta = 0.8
#TODO: we should feed it inputs to base its prediction on.
for i in range(100):
    my_nn.predict()
    my_nn.printOutputs()
    outputs = my_nn.getOutputs()
    total_error = mse(outputs)
    print('Error: '+str(total_error))
    #Learn
    backpropagate(my_nn, eta)