import random

class Perceptron:

    weights = None
    threshold = 2

    def output(self, input) :
        sum = 0
        i = 0
        while i < len(input):
            sum = sum + input[i] * self.weights[i]
            i += 1
        if sum > self.threshold:
            return 1
        else :
            return 0
    def train(self, inputs,  outputs_soll,  threshold,  lrate,  epochen):
        self.threshold = threshold
        n = len(inputs[0])
        p = len(outputs_soll)
        self.weights = [0.0] * (n)
        i = 0
        while (i < n) :
            self.weights[i] = random.uniform(0,1)
            i += 1
        i = 0
        while (i <= epochen) :
            totalError = 0
            j = 0
            while (j < p) :
                output_ist = self.output(inputs[j])
                error = outputs_soll[j] - output_ist
                totalError = totalError + abs(error)
                k = 0
                while (k < n) :
                    delta = lrate * inputs[j][k] * error
                    self.weights[k] = self.weights[k] + delta
                    k += 1
                j += 1
            print(f"Epoche {i}: total error {totalError}")
            if (totalError == 0) :
                break
            i += 1