#write a function f(x) that returns that square of x. Plot it for x values of -100 to 100 in increments of 1
from matplotlib import pyplot

def f(x):
    return(x**2)

def run():
    xs = list(range(-100, 101))
    ys = []
    for x in xs:
        ys.append(f(x))

    pyplot.plot(xs, ys)
    pyplot.show()

if __name__ == "__main__":
    run()
    