import numpy as np


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    A = np.random.randn(4, 3)
    B = np.sum(A, axis=1, keepdims=True)
    print(A)
    print(B)

    for (i in range(1, len(layer_dims) / 2)):
        parameter[‘W’ + str(i)] = np.random.randn(layers[i], layers[i - 1])) *0.01
        parameter[‘b’ + str(i)] = np.random.randn(layers[i], 1) * 0.01