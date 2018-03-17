# Write a function f(x) that returns the sin of x. Hint: there is a sin function in the math module. Plot it from -5 to 5 in increments of 1
from matplotlib import pyplot
import math 

def f(x):
    return math.sin(x)

def run():
    xs = list(range(-5, 6))
    ys = []
    for x in xs:
        ys.append(f(x))

    pyplot.plot(xs, ys)
    pyplot.show()

if __name__ == "__main__":
    run()
