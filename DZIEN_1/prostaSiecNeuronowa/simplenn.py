import numpy as np

class SimpleNeuralNetwork:
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(SimpleNeuralNetwork)

    #komentowanie/odkomentowanie bloku kodu: CTRL + /
    #duplikowanie bloku kodu: CTRL + D

    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1

    def __repr__(self):
        return (f"nowa siec neuronowa oparta na klasie: {self.__class__.__name__}\n"
                f"Wylosowano wagi (ziarno = 1):\n{self.weights}")
    
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    def d_sigmoid(self,x):
        return x*(1-x)
    
    def propagation(self,inputs):
        return self.sigmoid(np.dot(inputs.astype(float),self.weights))
    
    def backward_propagation(self,propagation_result,train_input,train_output):
        error = train_output - propagation_result
        self.weights += np.dot(train_input.T,error*self.d_sigmoid(propagation_result))
        
    def train(self,train_input,train_output,train_iters):
        for _ in range(train_iters):
            propagation_result = self.propagation(train_input)
            self.backward_propagation(propagation_result,train_input,train_output)
