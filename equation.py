def exp(x):
    e = 2.7182818285
    return pow(e, x)


def f(x):
    #    return pow(x - 4, 2) - 2
    return 5 * exp(-5 * x) - pow(x, 3) / 2 - 4


def derivative(x):
    #    return 2 * x - 8
    return -25 * exp(-5 * x) - 3 * pow(x, 2) / 2


def next(x):
    return x - f(x) / derivative(x)


def get_start():
    """Calculate interval where root is located.

    Stars from zero and checks intervals  like:
    (0 - eps, 0 + eps) where eps is bigger then
    step. If checking fails then distinct of 
    -1, 1, -2, 2, etc.
    """
    shift = 0
    step = 0.01
    eps = 1.1 * step
    i = 0                           # even parity flag
    while f(shift - eps) * f(shift + eps) >= 0:
        shift = -shift
        if i % 2 == 0:
            shift += step
        i += 1
    return (shift + eps, shift - eps, shift)


def main():
    precision = 0.00001
    start, end, val = get_start()
    current = next(val)
    steps = 1

    while (abs(val - current) > precision):
        steps += 1
        val = current
        current = next(val)
    root = current

    print("Root location interval: ({:.5f}, {:.5f})".format(start, end))
    print("Root: {:.5f}".format(root))
    print("Steps: {:d}".format(steps))
    print("f({:.5f}) = {:.5f}".format(root, f(root)))

if __name__ == '__main__':
    main()
