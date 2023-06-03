import random
import math

and_dataset = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
]
or_dataset = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

nand_dataset = [
    [0, 0, 1],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
def sigmoid(x):
    return 1/(1+math.exp(-x))

def train(dataset):
    w1 = random.random()
    w2 = random.random()
    b = random.random()
    absolute = 0.01
    rate = 0.01



    def cost(w1, w2, b):
        result = 0
        for x in dataset:
            y = sigmoid(w1 * x[0] + w2 * x[1] + b)
            d = y - x[2]
            result += d * d

        return result / len(dataset)

    lowest = cost(w1,w2, b)

    for n in range(1, 100000):
        c = cost(w1, w2, b)
        dw1 = (cost(w1 + absolute, w2,b) - c) / absolute
        dw2 = (cost(w1, w2 + absolute,b) - c) / absolute
        
        db = (cost(w1, w2,b + absolute) - c) / absolute
        
        if lowest > c:
            lowest = c
            opw1 = w1
            opw2 = w2
            opb = b

        # print(f"{w1}  {w2} {b} {cost(w1,w2,b)}")
        w1 -= rate * dw1
        w2 -= rate * dw2
        b -= rate * db

    return [w1, w2, b]

def check(res):
    for x in [0,1]:
        for y in [0,1]:
            print(f"{x} | {y} | {sigmoid(res[0]*x+res[1]*y+res[2])}")

print("And Gate")
check(train(and_dataset))


print("Or Gate")
check(train(or_dataset))


