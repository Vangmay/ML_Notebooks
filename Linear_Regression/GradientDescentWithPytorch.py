import torch
from functools import partial

def f(x):
    return ((4*x**2) + (2 * x) + 3) ## 4x^2 + 2x + 3

def quad(a,b,c,x):
    return(a*x**2 + b*x + c)

def make_quad(a, b, c):
    return partial(quad, a, b, c)

x = torch.linspace(-2, 2, steps=20)[:,None]
y = f(x)

def mae(preds, acts):
    return (torch.abs(preds - acts)).mean()
def LOSS(params):
    func = make_quad(*params)
    return mae(func(x), y)


abc = torch.tensor([1.5, 1.5, 1.5])
abc.requires_grad_()

for i in range(6):
    Loss = LOSS(abc)
    Loss.backward()
    with torch.no_grad():
        abc -= abc.grad * 0.1
        print("LOSS: ", Loss, "ABC: ", abc)