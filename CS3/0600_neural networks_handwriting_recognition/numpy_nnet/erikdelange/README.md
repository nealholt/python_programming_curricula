# Neural networks in numpy

A neural network can be created just by using numpy. No high level frameworks are needed. This can be helpful when trying to understand how a neural network actually works. This repository provides some hand-crafted examples. I devised them while diving into the details of networks. Of course when actually building a network I take an easier route using libraries like Keras. 

#### Datasets
In all examples I assume the use of supervised learning. For supervised learning datasets are needed which specify inputs and the corresponding output. File *dataset.py* contains a number of exercise datasets. The simplest ones are truth tables for logical functions like XOR. A variant is a 2x2 pixel image which can contain several shapes (here I distinguish vertical, horizontal and diagonal lines). To make life a bit more interesting the images are not only black and white (i.e. 1's and 0's) but can be turned into grayscale images where the shade of gray is a scalar ranging from 0 to 1.

#### Inference only
For starters I have created a few ready to use networks. A neural network consists of layers containing nodes. Each node has inputs, weights and a bias. The output of a node is the sum of every input * its weight plus the bias value. There are two ways to code this in numpy: specifying the bias as a separate value, or considering the bias as a weight which always has an input of 1. Files *2x2_image_predefined_1|2.py* show both approaches. Weights and biases are already determined elsewhere (and work for almost monochrome images), so the code only needs to do a forward pass through the network to translate the input into output. The image below gives a graphical representation.

![](https://github.com/erikdelange/Neural-networks-in-numpy/blob/master/2x2.png)

To avoid that the network can only approximate a linear function transfer or activation functions are needed. A set to use can be found in file *activation.py*. It is the non-linear nature of these functions which make a neural network do its cool things.  

#### Training  
In contrast to the examples above normally training the network is required to determine the weight and bias values. The basic approach how to find these is to do a forward pass through the network and then back-propagate the errors, adjusting weights and biases proportionally. File *xor.py* gives the basic setup how to do this for a two layer network. Note that it does not matter how many nodes per layer there are, the code stays the same. Using the derivative of the activation function might seem confusing. Its importance is to determine the direction of the error so we know how to adjust the weights.

For a three layer network example see *2x2_image_recognition.py*.

A generic approach - where the number of layers, nodes per layer and activation function per layer are not hard-coded but configurable - can be found in *network1.p*. 

#### Function approximation
In essence a neural network provides a function approximation where the function can be complex. For a linear function only one node is required. See *linear.py* for the approximation of y = ax + b. For polynomial functions of a degree above 1 we need more nodes. See *cubic.py* for an example of a degree of 3. The figure below shows how a neural network with a single hidden layer of 8 nodes can approximate function x^3 + 15x
 

![](https://github.com/erikdelange/Neural-networks-in-numpy/blob/master/cubic.png)