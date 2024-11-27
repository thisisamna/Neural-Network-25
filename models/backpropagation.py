import numpy as np


class BackPropagation:
    def __init__(self, learning_rate, layers, epochs, neurons, isBias=False, isSigmoid=True):
        self.learning_rate = learning_rate
        self.layers = layers
        self.epochs = epochs
        self.isBias = isBias
        self.isSigmoid = isSigmoid
        self.neurons = neurons  # list [3] or [4 3] layer 1 layer 2
        self.output_forward = []
        self.weights = [] #amira bthbd wla eh
        self.bias = []
        self.z_values = []

    """
    Thinking 
    we have 
     5 features 
     suppose 2 layers neurons/layer [3 4] 
     layer weight = (current layer neurons , pervious layer neurons)   
     first layer weights (3,5) dot X (90, 5).T  = (3,90)
     second layer weights (4,3) dot (3,90)  = (4,90)    
     output layer wights (3,4) dot (4,90) = (3,90)   
    """

    def get_sizes(self, X, Y):
        # X shape(90, 5)
        self.input_size = X.shape[1]
        self.output_size = Y.shape[1]
        self.hidden_size = self.neurons

    def initialize_params(self, X, Y):
        self.weights = [0.01 * np.random.randn(self.hidden_size[0], self.input_size)]
        if self.isBias == True:
            self.bias = [0.01 * np.random.randn(self.hidden_size[0])]
        else:
            self.bias = None

        for i in range(1, self.layers):
            self.weights.append(0.01 * np.random.randn(self.hidden_size[i], self.hidden_size[i - 1]))
            if self.isBias == True:
                self.bias.append(0.01 * np.random.randn(self.hidden_size[i]))

        self.weights.append(0.01 * np.random.randn(self.output_size, self.hidden_size[self.layers - 1]))  # [[-1]
        self.bias.append(0.01 * np.random.randn(self.output_size))
        # print("hidden weights list len", len(self.weights) )
        # print( self.weights)
        # print("all hidden BIAS shape",len(self.bias))
        # print( self.bias)
        # print("all output weights list len",len(self.weights_output))
        # print( self.weights_output)
        # print("all output BIAS list len",len(self.bias_output))
        # print( self.bias_output)

    # implement from Scratch
    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def tanh(self, Z):
        return (np.exp(Z) - np.exp(-Z)) / (np.exp(Z) + np.exp(-Z))

    def sigmoid_derivative(self, Z):
        sigmoid_Z = self.sigmoid(Z)
        return sigmoid_Z * (1 - sigmoid_Z)

    def tanh_derivative(self, Z):
        tanh_Z = self.tanh(Z)
        return 1 - tanh_Z ** 2

    def forward(self, X):
        print("Forward prop!")
        input_data = X
        # (3,5)  , (90,5)
        self.z_values.append(np.dot(self.weights[0], input_data.values) + (self.bias[0] if self.isBias else 0))
        self.output_forward.append(self.sigmoid(self.z_values[0]) if self.isSigmoid else self.tanh(self.z_values[0]))
        input_data = self.output_forward[0]
        print(self.z_values[0].shape)
        for i in range(1, self.layers+1):
            self.z_values.append(np.dot(self.weights[i], input_data.T) + (self.bias[i] if self.isBias else 0))
            if self.isSigmoid:
                self.output_forward.append(self.sigmoid(self.z_values[i]))
            else:
                self.output_forward.append(self.tanh(self.z_values[i]))

            input_data = self.output_forward[i]
        
        for i in range(3):
            print("layer", i + 1)
            print("Z values layer  shape", self.z_values[i].shape)
            print("output_forward shape", self.output_forward[i].shape)


    def backward(self, x, y):
        output = self.output_forward[-1]
        deltas = [0] * (self.layers + 1)
        deltas[-1] = (y.T - output) * output * (1 - output)

        for i in reversed(range(self.layers + 1)):
            if i == self.layers:
                delta_sum = np.dot(deltas[-1], self.weights_output.T)
            else:
                delta_sum = np.dot(deltas[i + 1], self.weights[i].T)
            deltas[i] = self.output_forward[i] * (1 - self.output_forward[i]) * delta_sum
            if i == self.layers - 1:
                self.weights_output -= x[i] * deltas[-1]
            else:
                self.weights[i] -= x[i] * deltas[i]

    def train(self, X, Y):
        self.get_sizes(X, Y)
        self.initialize_params(X, Y)
        self.forward(X.iloc[0,:])
        #self.backward(X, Y)
        # for i in range(self.layers):
        #     self.backward(X, y)


    def predict():
        print()

