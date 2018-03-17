#Now it's pretty tho

from matplotlib import pyplot
import math 
from numpy import arange

def f(x):
    return math.sin(x)

def run():
    xs = list(arange(-5, 6, 0.1))
    ys = []
    for x in xs:
        ys.append(f(x))

    pyplot.plot(xs, ys)
    pyplot.show()

if __name__ == "__main__":
    run()
