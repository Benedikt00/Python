import random

class Perceptron:

    weights = None
    threshold = 2

    def output(self, input) :
        sum = 0

        for i in range(len(input)):
            sum = sum + input[i] * self.weights[i]

        if sum > self.threshold:
            return 1
        else :
            return 0
    def train(self, inputs,  outputs_soll,  threshold,  lrate,  epochen):

        self.threshold = threshold
        n = len(inputs[0])
        p = len(outputs_soll)
        self.weights = [0.0] * (n)

        for i in range(n):
            self.weights[i] = random.uniform(0,1)

        for i in range(epochen):
            totalError = 0

            for j in range(p):
                output_ist = self.output(inputs[j])
                error = outputs_soll[j] - output_ist
                totalError = totalError + abs(error)

                for k in range(n):
                    delta = lrate * inputs[j][k] * error
                    self.weights[k] = self.weights[k] + delta
                    k += 1
                j += 1
            print(f"Epoche {i}: total error {totalError}")
            if (totalError == 0) :
                break
