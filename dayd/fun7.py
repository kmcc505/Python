#write a function that converts temps from F to C and plot on a graph
#Now it's pretty tho

from matplotlib import pyplot
import math 
from numpy import arange

def f(x):
    return (x * 1.8) + 32

def run():
    xs = list(arange(1, 37))
    ys = []
    for x in xs:
        ys.append(f(x))

    pyplot.plot(xs, ys)
    pyplot.show()

    
if __name__ == "__main__":
    run()
