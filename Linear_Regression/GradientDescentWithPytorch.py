import torch 
from functools import partial
import random

def f(x):
    """
    Original function we want to predict
    """
    return ((2*x) + 5)

def linear(M,C,X):
    return ((M*X) + C)

def make_function(M, C):
    """
    Returns a partial function
    based on parameters M and C in the form of
    Y = Mx + C
    """
    return partial(linear, M, C)

def mae(preds, acts):
    return (torch.abs(preds-acts)).double().mean()

x = torch.arange(1, 1000)
Y = f(x) 


def LOSS(params):
    """
    Creates a function out of the parameters and calculates 
    the loss by comparing it to the original function
    """
    print(params)
    f = make_function(*params)
    return mae(f(x), Y)

random_tensor = torch.tensor([0.03, 0.20])
random_tensor.requires_grad_()

for i in range(0,10):
    loss = LOSS(random_tensor)
    # Calculate gradients
    loss.backward()
    with torch.no_grad():
        random_tensor -= random_tensor.grad*0.01
    print(random_tensor)
