from math import cos, sin

DEBUG = True
t_width = 5
y_width = 10

if DEBUG:
    def f(t, y):
        return cos(t) + 1
else:
    def f(t, y):
        return t**2 + y**2


def solution(t, y):
    return t + sin(t)


def main():
    # Initial data
    t0 = 0
    y0 = 0
    h = 0.1
    steps = 30

    # The Runge–Kutta method(RK4)
    tn = t0
    yn = y0
    try:
        print("{:>{t_width}s} | {:>{y_width}s}".format(
            "t", "y", t_width=t_width, y_width=y_width))
        print("-" * (t_width + y_width + 3))

        for i in range(steps):
            t_next = tn + h
            k1 = f(tn, yn)
            k2 = f(tn + h / 2, yn + h / 2 * k1)
            k3 = f(tn + h / 2, yn + h / 2 * k2)
            k4 = f(tn + h, yn + h * k3)
            y_next = yn + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            tn = t_next
            yn = y_next

            # Results displaying
            string = "{:>{t_width}g} | {:>{y_width}.6f}".format(
                tn, yn, t_width=t_width, y_width=y_width)
            print(string)
            if DEBUG:
                print("True y| {:10.6f}".format(solution(tn, yn)))
            print("-" * (t_width + y_width + 3))
    except OverflowError:
        print("Too large numbers.")

if __name__ == '__main__':
    main()
