'''
STEPS:
1 Figure out how to call the train function and write that code. Open up the article and maybe author's github links to try to figure out how he's feeding the data in with the X and Y matrices.
2 Download needed Python libraries
3 Write a loss function to apply this neural net to the handwriting assignment.
4 Get it working.


Source for this code: 
https://towardsdatascience.com/lets-code-a-neural-network-in-plain-numpy-ae7e74410795
Other resources from the author include:
https://github.com/SkalskiP/ILearnDeepLearning.py

The author mentions PyTorch as a powerful tool which might be worth investigating.

Other "Python Neural Nets from scratch" that might be worth looking into if this one doesn't pan out include:
https://github.com/erikdelange/Neural-networks-in-numpy
https://towardsdatascience.com/neural-net-from-scratch-using-numpy-71a31f6e3675
https://github.com/Msanjayds/DeepLearning/blob/master/Classficatin_NN%20vs%20LogisticReg.ipynb
https://www.python-course.eu/neural_networks_with_python_numpy.php
'''



'''Each item in the list is a dictionary describing the basic parameters of a single network layer: input_dim - the size of the signal vector supplied as an input for the layer, output_dim - the size of the activation vector obtained at the output of the layer and activation - the activation function to be used inside the layer.'''
nn_architecture = [
    {"input_dim": 2, "output_dim": 4, "activation": "relu"},
    {"input_dim": 4, "output_dim": 6, "activation": "relu"},
    {"input_dim": 6, "output_dim": 6, "activation": "relu"},
    {"input_dim": 6, "output_dim": 4, "activation": "relu"},
    {"input_dim": 4, "output_dim": 1, "activation": "sigmoid"},
]


def init_layers(nn_architecture, seed = 99):
    np.random.seed(seed)
    number_of_layers = len(nn_architecture)
    params_values = {}
    #the matrix W and vector b have been filled with small, random numbers.
    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        layer_input_size = layer["input_dim"]
        layer_output_size = layer["output_dim"]
        
        params_values['W' + str(layer_idx)] = np.random.randn(
            layer_output_size, layer_input_size) * 0.1
        params_values['b' + str(layer_idx)] = np.random.randn(
            layer_output_size, 1) * 0.1
    
    return params_values


'''There are many activation functions, but in this project I decided to provide the possibility of using two of them — sigmoid and ReLU. To be able to go full circle and pass both forward and backward propagation, we also have to prepare their derivatives.'''
def sigmoid(Z):
    return 1/(1+np.exp(-Z))
def relu(Z):
    return np.maximum(0,Z)
def sigmoid_backward(dA, Z):
    sig = sigmoid(Z)
    return dA * sig * (1 - sig)
def relu_backward(dA, Z):
    dZ = np.array(dA, copy = True)
    dZ[Z <= 0] = 0;
    return dZ;


'''Forward Propagation - The designed neural network will have a simple architecture. The information flows in one direction — it is delivered in the form of an X matrix, and then travels through hidden units, resulting in the vector of predictions Y_hat. To make it easier to read, I split forward propagation into two separate functions — step forward for a single layer and step forward for the entire NN.'''
def single_layer_forward_propagation(A_prev, W_curr, b_curr, activation="relu"):
    Z_curr = np.dot(W_curr, A_prev) + b_curr
    
    if activation is "relu":
        activation_func = relu
    elif activation is "sigmoid":
        activation_func = sigmoid
    else:
        raise Exception('Non-supported activation function')
    
    return activation_func(Z_curr), Z_curr


'''This part of the code is probably the most straightforward and easy to understand . Given input signal from the previous layer, we compute affine transformation Z and then apply selected activation function. By using NumPy, we can leverage vectorization — performing matrix operations, for the whole layer and whole batch of examples at once. This eliminates iteration and significantly speeds up our calculations. In addition to the calculated matrix A, our function also returns an intermediate value Z. What for? The answer is shown in Figure 2. We will need Z during the backward step.
Using a pre-prepared one layer step forward function, we can now easily build a whole forward propagation step. This is a slightly more complex function, whose role is not only to perform predictions but also to organize the collection of intermediate values. It returns, among other things, Python dictionary, which contains A and Z values computed for particular layers.'''
def full_forward_propagation(X, params_values, nn_architecture):
    memory = {}
    A_curr = X
    
    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        A_prev = A_curr
        
        activ_function_curr = layer["activation"]
        W_curr = params_values["W" + str(layer_idx)]
        b_curr = params_values["b" + str(layer_idx)]
        A_curr, Z_curr = single_layer_forward_propagation(A_prev, W_curr, b_curr, activ_function_curr)
        
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr
    
    return A_curr, memory


'''Loss Function - In order to monitor our progress and make sure that we are moving in right direction, we should routinely calculate the value of the loss function. “Generally speaking, the loss function is designed to show how far we are from the ‘ideal’ solution.” It is selected according to the problem we plan to solve, and frameworks such as Keras have many options to choose from. Because I am planning to test our NN for the classification of points between two classes, I decided to use binary crossentropy'''
#NOTE this is problem specific and should be changed for other problems!
def get_cost_value(Y_hat, Y):
    m = Y_hat.shape[1]
    cost = -1 / m * (np.dot(Y, np.log(Y_hat).T) + np.dot(1 - Y, np.log(1 - Y_hat).T))
    return np.squeeze(cost)

def get_accuracy_value(Y_hat, Y):
    Y_hat_ = convert_prob_into_class(Y_hat)
    return (Y_hat_ == Y).all(axis=0).mean()


'''Backward Propagation - Sadly, backward propagation is regarded by many inexperienced deep learning enthusiasts as algorithm that is intimidating and difficult to understand. The combination of differential calculus and linear algebra very often deters people who do not have a solid mathematical training. So don’t worry too much if you don’t understand everything right away. Trust me, we all went through it.'''
def single_layer_backward_propagation(dA_curr, W_curr, b_curr, Z_curr, A_prev, activation="relu"):
    m = A_prev.shape[1]
    
    if activation is "relu":
        backward_activation_func = relu_backward
    elif activation is "sigmoid":
        backward_activation_func = sigmoid_backward
    else:
        raise Exception('Non-supported activation function')
    
    dZ_curr = backward_activation_func(dA_curr, Z_curr)
    dW_curr = np.dot(dZ_curr, A_prev.T) / m
    db_curr = np.sum(dZ_curr, axis=1, keepdims=True) / m
    dA_prev = np.dot(W_curr.T, dZ_curr)
    
    return dA_prev, dW_curr, db_curr

'''Often people confuse backward propagation with gradient descent, but in fact these are two separate matters. The purpose of the first one is to calculate the gradient effectively, whereas the second one is to use the calculated gradient to optimize. In NN, we calculate the gradient of the cost function (discussed earlier) in respect to parameters, but backpropagation can be used to calculate derivatives of any function. The essence of this algorithm is the recursive use of a chain rule known from differential calculus — calculate a derivative of functions created by assembling other functions, whose derivatives we already know.'''
def full_backward_propagation(Y_hat, Y, memory, params_values, nn_architecture):
    grads_values = {}
    m = Y.shape[1]
    Y = Y.reshape(Y_hat.shape)
   
    dA_prev = - (np.divide(Y, Y_hat) - np.divide(1 - Y, 1 - Y_hat));
    
    for layer_idx_prev, layer in reversed(list(enumerate(nn_architecture))):
        layer_idx_curr = layer_idx_prev + 1
        activ_function_curr = layer["activation"]
        
        dA_curr = dA_prev
        
        A_prev = memory["A" + str(layer_idx_prev)]
        Z_curr = memory["Z" + str(layer_idx_curr)]
        W_curr = params_values["W" + str(layer_idx_curr)]
        b_curr = params_values["b" + str(layer_idx_curr)]
        
        dA_prev, dW_curr, db_curr = single_layer_backward_propagation(
            dA_curr, W_curr, b_curr, Z_curr, A_prev, activ_function_curr)
        
        grads_values["dW" + str(layer_idx_curr)] = dW_curr
        grads_values["db" + str(layer_idx_curr)] = db_curr
    
    return grads_values


'''The goal of this method is to update network parameters using gradient optimisation. In this way, we try to bring our target function closer to a minimum.'''
def update(params_values, grads_values, nn_architecture, learning_rate):
    for layer_idx, layer in enumerate(nn_architecture):
        params_values["W" + str(layer_idx)] -= learning_rate * grads_values["dW" + str(layer_idx)]        
        params_values["b" + str(layer_idx)] -= learning_rate * grads_values["db" + str(layer_idx)]
    
    return params_values;



def train(X, Y, nn_architecture, epochs, learning_rate):
    params_values = init_layers(nn_architecture, 2)
    cost_history = []
    accuracy_history = []
    
    for i in range(epochs):
        Y_hat, cashe = full_forward_propagation(X, params_values, nn_architecture)
        cost = get_cost_value(Y_hat, Y)
        cost_history.append(cost)
        accuracy = get_accuracy_value(Y_hat, Y)
        accuracy_history.append(accuracy)
        
        grads_values = full_backward_propagation(Y_hat, Y, cashe, params_values, nn_architecture)
        params_values = update(params_values, grads_values, nn_architecture, learning_rate)
        
    return params_values, cost_history, accuracy_history


