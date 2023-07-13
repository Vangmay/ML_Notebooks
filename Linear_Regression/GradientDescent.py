# Take derivative of the loss function with respect to each parameter
# Pick random values for parameters
# Plug parameter values into the derivatives
# Calculate the step sizes: Step size = slope x learning rate
# Calculate the new parameters: New params = old params - step 


def Loss(points, C, M):
    """
    Parametric function assumes that line is in the form Y = Mx + C 
    where M and C are the parameters to be changed
    Calculates the Cost by summing the squares of differences
    """
    Error = 0
    for i in range(0,len(points)):
        Error += (points[i] - ((i*M) + C))**2
    return Error / float(len(points))


def Step(points, C, M, learningRate):
    """
    This functions takes the mapping, Yintercept (C) and Slope(M) and calculates the step size based on partial derivatives
    Then the function returns the updated parameters C and M. 
    """
    dLdC, dLdM = 0,0 # Partial derivatives

    N = float(len(points))
    for X in range(0, len(points)):
        dLdC += -(2/N) * (points[X] -  (M * X) + C) 
        dLdM += -(2/N) * X * (points[X] - (M * X) + C)
    new_C = C - (learningRate * dLdC)
    new_M = M - (learningRate * dLdM)
    return [new_C, new_M]

def GradientDescent(points, C, M, LearningRate, Iterations):
    Final_C = C 
    Final_M = M 
    for i in range(0,Iterations):
        Final_C,Final_M = Step(points, Final_C, Final_M, LearningRate)
        print(f"Y = {Final_M}X + {Final_C} ERROR = {Loss(points, Final_C, Final_M)}")
    return [Final_C, Final_M]

# Points is an array where the index indicates the X value and the value within that index is the Y value.
points = [((i*5) + 3 ) for i in range(0,100)] 
C = 0 
M = 0
LearningRate = 0.0001
Iterations = 10000
GradientDescent(points, C, M, LearningRate, Iterations)