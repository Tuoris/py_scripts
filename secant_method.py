from math import cos
from sys import exit

MAX_LOOPS = 1000
PRECISION = 0.0001  # precision = 0.0001%


def f(x):
    return cos(x) + 1 / (x + 2)


def calc_precision(x, x_old):
    """Calculate precision as a proportion"""
    return abs((x - x_old) / x)


def loop(a, b, x):
    x_old = x
    fa = f(a)
    fb = f(b)
    x = a - fa * (b - a) / (fb - fa)
    fx = f(x)
    if fx * fa > 0:
        a = x
    else:
        b = x
    return (a, b, x, x_old)


def section(title):
    print('{0:-^{width}s}'.format(title, width=section_width))


def end_section():
    print(('-' * section_width) + '\n')

section_width = 40


def main():
    interval = (0, 3)
    a, b = interval
    h = 0.4

    fa = f(a)
    fb = f(b)

    if abs(fb) > abs(fa) and fa * fb > 0:
        h = -h
    b = a + h
    fb = f(b)

    # Looking for root at interval
    section(' Root localization ')
    while fa * fb > 0 and a >= interval[0] and b <= interval[1]:
        print("a = {:.2f}, b = {:.2f}".format(a, b))
        a = b
        b = a + h
        fa = f(a)
        fb = f(b)

    if a >= interval[0] and b <= interval[1]:
        print('Interval located : [{:.2f},{:.2f}]'.format(a, b))
    else:
        print('Interval not located!')
        print('Unable to find roots.\n')
        exit()
    end_section()

    # Main calculations
    section(' Secant method ')
    x = a
    a, b, x, x_old = loop(a, b, x)

    loops = 1
    while (calc_precision(x, x_old) * 100 > PRECISION or
           loops >= MAX_LOOPS):
        a, b, x, x_old = loop(a, b, x)
        print('x = {:.8f}, x_old = {:.8f}'.format(x, x_old))
        loops += 1
    end_section()

    # Result displaying
    section(' Result ')
    print('x = {:.8f}, f(x) = {:.8f}'.format(x, f(x)))
    print('Defined precision: {}%'.format(PRECISION))
    print('Current precision: {:%}'.format(calc_precision(x, x_old)))
    print('Loops: {}'.format(loops))
    end_section()

if __name__ == '__main__':
    main()
