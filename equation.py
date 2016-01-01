def exp(x):
    e = 2.7182818285
    return pow(e, x)

def function(x):
#    return pow(x - 4, 2) - 2
    return 5 * exp(-5 * x) - pow(x, 3) / 2 - 4

def derivative(x):  
#    return 2 * x - 8
    return -25 * exp(-5 * x) - 3 * pow(x, 2) / 2

def next(x):
    return x - function(x) / derivative(x)

def get_start():
    shift = 0                       # starting from zero
    step = 0.01                     # adding this step
    eps = step + 0.1 * step         # range will have size 2*eps
    i = 0                           # even parity flag
    while function(shift - eps)*function(shift + eps) >= 0:
        shift = -shift
        if i % 2 == 0:
            shift += step
        i += 1
    return (shift + eps, shift - eps, shift)

def main():
    precision = 0.00001
    start, end, val = get_start()
    current = next(val)
    steps = 1   # iteration couter

    while (abs(val - current) > precision):
        steps += 1
        val = current
        current = next(val)
    root = current

    print("\nRange (%.5f, %.5f)" % (start, end))
    print("Root: %.5f" % root)
    print("Steps: %d" % steps)
    print("f(%.5f) = %.5f" % (root, function(root)))

if __name__ == '__main__':
    main()
