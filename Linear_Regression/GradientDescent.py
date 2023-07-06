
# Take derivative of the loss function with respect to each parameter
# Pick random values for parameters
# Plug parameter values into the derivatives
# Calculate the step sizes: Step size = slope x learning rate
# Calculate the new parameters: New params = old params - step 


import random 
f = {i : (i*2 + 3) for i in range(0,1000)}
points = f 


def Loss(Yintercept, Slope ,points):
    totalError = 0 
    for i in range(0,len(points)):
        totalError += (points[i] - ((Slope * i) + Yintercept)) ** 2    
    return (totalError)

def ErrorAtAPoint(Points, i, Yintercept, Slope):
    TrueX = i 
    TrueY = Points[i]
    PredictedY = (Slope * i) + Yintercept
    return (TrueY - PredictedY)

def Step(Yintercept, Slope, points, learningRate):
    dlDm , dlDs = 0,0  
    N = float(len(points))
    for i in range(0,len(points)):
        dlDm = -2 * ErrorAtAPoint(points, i, Yintercept, Slope) # Relates how the Loss changes as the intercept changes
        dlDs = -2 * i * ErrorAtAPoint(points, i, Yintercept, Slope ) 
    newIntercept = Yintercept - (dlDm * learningRate)
    newSlope = Slope - (dlDs * learningRate)
    return [newIntercept, newSlope]

def GradientDescent(Yintercept, Slope, iterations, points, learningRate):
    for i in range(0,iterations):
        b,m = Step(Yintercept, Slope, points, learningRate)
    return [b,m]

def Start():
    points = f 
    learningRate = 0.0000005
    Yintercept = 0
    Gradient = 0
    iterations = 20000
    [b,m] = GradientDescent(Yintercept, Gradient, iterations, points, learningRate)
    print(f"Y = {m}X + {b}")

Start()