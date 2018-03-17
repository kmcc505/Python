# Write a function f(x) that returns 1 if x is odd and -1 if x is even. Plot it for x values of -5 to 5 in increments of 1

from matplotlib import pyplot

def f(x):
    if x % 2 != 0:
        return(1)
    if x % 2 == 0:
        return(-1)

def run():
    xs = list(range(-5, 6))
    ys = []
    for x in xs:
        ys.append(f(x))

    pyplot.bar(xs, ys)
    pyplot.show()

if __name__ == "__main__":
    run()
    
    