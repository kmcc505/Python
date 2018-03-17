from matplotlib import pyplot

def f(x):
    return(x+1)

def run():
    xs = list(range(-3, 4))
    ys = []
    for x in xs:
        ys.append(f(x))

    pyplot.plot(xs, ys)
    pyplot.show()

if __name__ == "__main__":
    run()