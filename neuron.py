dataset = [
    [1,3],
    [2,6],
    [3,9],
    [4,12],
    [5,15]
]

# our model
# y = w* x + b 

actualNumber = dataset[0][1]/dataset[0][0]
w = 2 #initial assumed value
b = 1
const = rate = 0.00001

# Here the average of distance squared is taken
def costFunc(w :int, b :int ):
    result = 0
    # print(f"param = {w}")
    for x in dataset:
        act_y = w * x[0] + b
        exp_y = x[1]
        # print(f"Actual = {act_y} || Expected = {exp_y}")
        dist = act_y - exp_y
        result += dist*dist
    return result/len(dataset)

# derivative of the parabola gives us the lowest possible value
dw = (costFunc((w+const) , b) - costFunc(w,b))/const
db = (costFunc(w , (b+const)) - costFunc(w,b))/const
lowest = costFunc(w, b)

#iteration to get closer to actual value
for i in range(0,1000):
    w -= rate*dw
    b -= rate*db
    if lowest > costFunc(w,b):#picking the value that gives us the lowest cost
        lowest = costFunc(w,b)
        magicalNumber = w
        bias = b

    # print(costFunc(w))

print("-----------------------")
print(magicalNumber, bias)
print(f"Our model is {(1 - ( abs(actualNumber - (magicalNumber*1+bias))/actualNumber))*100}% accurate.")
for x in dataset:
    print(f"{x[0]} | {x[1]} | {x[0]*magicalNumber + bias}")