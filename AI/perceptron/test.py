from with_for import *

inputs = [[0, 0], [1, 0], [0, 1], [1, 1]]
outputs = [0, 0, 0, 1]

p_and = Perceptron()
p_and.train(inputs, outputs, 0.2, 0.1, 200)
print("ergebniss 0 0 = " + str(p_and.output([0, 0])))