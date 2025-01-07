print("prosty model sieci neuronowej!")
import numpy as np
from simplenn import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0]])
train_outputs = np.array([[1,0,1,1,0,1]]).T
train_iterators = 50_000

network.train(train_inputs,train_outputs,train_iterators)
print(f"wytrenowane wagi:\n{network.weights}")

print("____________ ocena modelu __________")
testdata = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]])

for data in testdata:
    print(f"wynik dla {data} wynosi: {network.propagation(data)}")

